# OpenSpot

A simple Spotify playlist downloader web application built using the Flask framework. It allows you to input a Spotify playlist URL and download the songs in the playlist as audio files using the youtube-dl library.

## Prerequisites
Before using this application, you need to have the following dependencies installed:
- Python 3
- Flask
- Spotipy
- ytdl

You can install these dependencies using pip:
```
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository to your local machine:
```
git clone https://github.com/riz4d/OpenSpot
```
2. Create a Spotify Developer Application and obtain your API credentials (Client ID and Client Secret). You can create an application [here](https://developer.spotify.com/dashboard/applications).

3. A config.py file in the directory and add your Spotify API credentials:
```
client_id = "your-client-id"
client_secret = "your-client-secret"
```
4. Run the Flask application:
   ```
   python3 app.py
   ```
   The app should be running at localhost