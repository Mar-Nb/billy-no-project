from platform import release
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = spotify.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

def getTrackFeatures(id):
    track_info = spotify.track(id)
    features_info = spotify.audio_features(id)
    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    audio = track_info['preview_url']
    cover = track_info['album']['images'][0]['url']
    print(name, " ", audio)

track_ids = getTrackIDs('Kuraihani', 'https://open.spotify.com/playlist/4IQUdsVry6H16OT9e19Ldz?si=e9d46678736c4cbc')
#print(track_ids)

for track_id in track_ids:
    getTrackFeatures(track_id)
