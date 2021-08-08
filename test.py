import os, requests, json, pickle, re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

secrets = []

def load_secrets(filename):
    global secrets
    with open(filename, "r") as f:
        secrets = json.load(f)

def main():
    load_secrets("secrets.json")
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
                                    client_id=secrets["client_id"],
                                    client_secret=secrets["client_secret"]
                            ))
    
if __name__ == '__main__':
    main()


