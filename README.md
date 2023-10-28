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

## Usage

1. Open your web browser and go to
   ```
   http://localhost
   ```
2. Enter a valid Spotify playlist URL in the input field and click the "Download" button.

3. The application will use the Spotify API to fetch the track list from the playlist and pass the track names to ytdl and songs been start downloads

4. You can check the progress of the downloads on the web page.

## Note

- This application is for educational purposes only and should only be used to download songs you have the legal right to access and use.

- The legality of downloading music from YouTube varies by jurisdiction. Be sure to review and comply with your local copyright laws.

- Be respectful of the rights of content creators and use this tool responsibly.
