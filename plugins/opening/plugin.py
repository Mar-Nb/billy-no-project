from copyreg import constructor
import sys
from platform import release
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
sys.path.append('../../')
from pluginDefault import PluginDefault

class PluginOpening(PluginDefault):

    def response(self, sentence=""):
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        dictionnaire = dict()       
        try:
            # récupère les animes et les liens de leur playlist
            f = open('./Opening.json')
            animes = json.load(f)
            anime = animes[sentence.replace("Opening ", "").replace("opening ", "").replace("op ", "").replace("OP ", "")]
            
            # récupère les opening de la playlist
            track_ids = []
            playlist = spotify.user_playlist("Kuraihani", anime)
            for item in playlist['tracks']['items']:
                track = item['track']
                track_ids.append(track['id'])

            # récupère les informations de chaque opening
            for track_id in track_ids:

                track_info = spotify.track(track_id)
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
                json_string = json.dumps(dictionnaire, ensure_ascii=False).encode("utf8")
            return json_string.decode()
        except Exception:
            error_string = json.dumps('{"error": "Votre anime ne fais pas partie de la liste"}', ensure_ascii=False).encode("utf8")
            return error_string.decode()

    