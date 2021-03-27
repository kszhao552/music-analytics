import spotipy
import spotipy.oauth2 as oauth2
import json

class Spotify(object):
    """description of class"""

    def __init__(self):
        with open('Keys.json', 'r') as f:
            config = json.load(f)
 
        client = config['client']
        secret = config['secret']

        credentials = oauth2.SpotifyClientCredentials(client_id = client, client_secret = secret)

        token = credentials.get_access_token()
        self.sp = spotipy.Spotify(auth = token)
        
    def getTrack(self, track, artist):
        return self.sp.search(q=f'artist: {artist[0]} track: {track}', type = 'track', limit =1)

    def getTrackTitle(self, track):
        return self.sp.search(q=f'track: {track}', type = 'track', limit =1)

    def getAudioFeatures(self, id):
        return self.sp.audio_features(id)
    