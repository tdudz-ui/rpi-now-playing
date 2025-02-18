# app.py - Flask backend
from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Spotify API Authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-currently-playing user-modify-playback-state"
))

app = Flask(__name__)

def get_current_track():
    try:
        track = sp.current_user_playing_track()
        if track and track.get("item"):
            return {
                "name": track["item"]["name"],
                "artist": ", ".join([artist["name"] for artist in track["item"]["artists"]]),
                "album_art": track["item"]["album"]["images"][0]["url"],
                "progress_ms": track["progress_ms"],
                "duration_ms": track["item"]["duration_ms"]
            }
    except Exception as e:
        print(f"Error fetching track: {e}")
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/now_playing")
def now_playing():
    track = get_current_track()
    return jsonify(track) if track else jsonify({"error": "No song playing"})

@app.route("/play")
def play():
    try:
        sp.start_playback()
        return jsonify({"status": "Playing"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/pause")
def pause():
    try:
        sp.pause_playback()
        return jsonify({"status": "Paused"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/next")
def next_track():
    try:
        sp.next_track()
        return jsonify({"status": "Next track"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/previous")
def previous_track():
    try:
        sp.previous_track()
        return jsonify({"status": "Previous track"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
