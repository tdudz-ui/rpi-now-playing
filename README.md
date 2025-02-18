# Spotify Now Playing Display

This project is a web-based **Spotify Now Playing** display designed to run on a **Raspberry Pi Zero W**. It fetches currently playing song details from your Spotify account and displays them with album art, a progress bar, and playback controls.

## Features

- 🎵 Displays the current song title, artist, and album art.
- 🎨 Album art as a blurred background for a sleek UI.
- ⏯️ Play/Pause, Next, and Previous track controls.
- 📊 Progress bar indicating song duration.
- 🔄 Auto-refreshes every 5 seconds.

## Installation

### 1️⃣ **Set Up Raspberry Pi**

1. Install **Raspberry Pi OS Lite** and set up Wi-Fi & SSH.
2. SSH into the Pi:
   ```bash
   ssh pi@raspberrypi.local
   ```

### 2️⃣ **Install Dependencies**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 3️⃣ **Clone This Repository & Set Up Environment**

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/spotify-now-playing.git
cd spotify-now-playing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4️⃣ **Set Up Spotify API Credentials**

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Create a new app and get the **Client ID** & **Client Secret**.
3. Set the **Redirect URI** to `http://localhost:5000/callback`.
4. Create a `.env` file:
   ```bash
   nano .env
   ```
   Add:
   ```
   SPOTIPY_CLIENT_ID="your_client_id"
   SPOTIPY_CLIENT_SECRET="your_client_secret"
   SPOTIPY_REDIRECT_URI="http://localhost:5000/callback"
   ```

### 5️⃣ **Run the Web App**

```bash
flask run --host=0.0.0.0 --port=5000
```

- Open a web browser and go to `http://raspberrypi.local:5000`.

### 6️⃣ **Auto-Start on Boot**

1. Open **crontab**:
   ```bash
   crontab -e
   ```
2. Add this line:
   ```
   @reboot cd /home/pi/spotify-now-playing && source venv/bin/activate && flask run --host=0.0.0.0 --port=5000 &
   ```

## Usage

- Open the web interface to see the currently playing song.
- Use the **play/pause, next, and previous** buttons to control playback.
- The UI updates every 5 seconds to stay in sync with Spotify.

## Contributing

Pull requests and suggestions are welcome! If you find a bug or have a feature request, open an issue.

## License

This project is licensed under the **MIT License**.

🚀 Enjoy your Spotify Now Playing display!

