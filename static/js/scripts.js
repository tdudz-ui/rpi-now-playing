// scripts.js - Frontend logic
async function fetchNowPlaying() {
    const response = await fetch("/now_playing");
    const data = await response.json();
    document.getElementById("album-art").src = data.album_art;
    document.getElementById("song-title").textContent = data.name;
    document.getElementById("artist-name").textContent = data.artist;
}

setInterval(fetchNowPlaying, 5000);
fetchNowPlaying();
