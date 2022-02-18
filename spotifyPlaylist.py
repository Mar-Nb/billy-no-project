from platform import release
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

dictionnaire = dict()

def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = spotify.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

def getTrackFeatures(id):
    track_info = spotify.track(id)
    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    audio = track_info['preview_url']
    cover = track_info['album']['images'][0]['url']
    dictionnaire[name] = dict()
    dictionnaire[name]["album"] = album
    dictionnaire[name]["artist"] = artist
    dictionnaire[name]["audio"] = audio
    dictionnaire[name]["cover"] = cover

anime = "Bleach"
f = open('./Opening.json')
animes = json.load(f)

track_ids = getTrackIDs('Kuraihani', animes[anime])

for track_id in track_ids:
    getTrackFeatures(track_id)

print(dictionnaire)