import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .youtubedll import youtube_search
from .zip import zip_folder
from config import client_id,client_secret
import pyrebase
import os
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
firebaseConfig = {
    "apiKey": "AIzaSyAwxPxgTGwtUqU9PEB2C6OkWUwb4U01EZw",
    "authDomain": "amldetect.firebaseapp.com",
    "databaseURL": "https://amldetect-default-rtdb.firebaseio.com",
    "projectId": "amldetect",
    "storageBucket": "amldetect.appspot.com",
    "messagingSenderId": "723421749108",
    "appId": "1:723421749108:web:53bc8e7922a82ae0189621",
    "measurementId": "G-HBF7MEYJ6N"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def play_fetch(playlist_id):
        
    try:
        playlist = sp.playlist(playlist_id)

        PlaylistName = f"Playlist Name: {playlist['name']}"
        Owner = f"Owner: {playlist['owner']['display_name']}"
        TotalTracks = f"Total Tracks: {playlist['tracks']['total']}"
        return PlaylistName,Owner,TotalTracks
    except Exception as e:
        print(f"An error occurred: {e}")
def playlist_dl(playlist_id,req_id):
    
    try:
        playlist = sp.playlist(playlist_id)

        PlaylistName = f"Playlist Name: {playlist['name']}"
        Owner = f"Owner: {playlist['owner']['display_name']}"
        TotalTracks = f"Total Tracks: {playlist['tracks']['total']}"

        print("Tracks:")
        for idx, track in enumerate(playlist['tracks']['items']):
            track_info = track['track']
            track_name = track_info['name']
            artists = [artist['name'] for artist in track_info['artists']]
            artists_str = ", ".join(artists)
            youtube_search(f"{track_name} - {artists_str}",req_id)
            print(f"{idx + 1}. {track_name} - {artists_str}")
        zip_folder(f"./media/{req_id}",f"./media/{req_id}/playlist.zip")
        storage.child(f"spotify/{req_id}/playlist.zip").put(f"./media/{req_id}/playlist.zip")
        path_media = storage.child(f"spotify/{req_id}/playlist.zip").get_url(None)
        
        return path_media,f"./media/{req_id}",TotalTracks,Owner,PlaylistName
    except Exception as e:
        print(f"An error occurred: {e}")
