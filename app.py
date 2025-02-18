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

app = Flask(__name__)

SPOTIPY_CLIENT_ID = "your_client_id"
SPOTIPY_CLIENT_SECRET = "your_client_secret"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-read-currently-playing user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

def get_current_track():
    track = sp.current_user_playing_track()
    if track is not None:
        return {
            "name": track["item"]["name"],
            "artist": ", ".join([artist["name"] for artist in track["item"]["artists"]]),
            "album_art": track["item"]["album"]["images"][0]["url"],
            "progress_ms": track["progress_ms"],
            "duration_ms": track["item"]["duration_ms"]
        }
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
    sp.start_playback()
    return jsonify({"status": "Playing"})

@app.route("/pause")
def pause():
    sp.pause_playback()
    return jsonify({"status": "Paused"})

@app.route("/next")
def next_track():
    sp.next_track()
    return jsonify({"status": "Next track"})

@app.route("/previous")
def previous_track():
    sp.previous_track()
    return jsonify({"status": "Previous track"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
