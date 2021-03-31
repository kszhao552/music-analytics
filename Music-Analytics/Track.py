import re
import spotipy
import spotipy.oauth2 as oauth2

class Track:
    def __init__ (self, rank, name, artist, year):
        self.name = name
        self.rank = rank
        self.artist = re.split(', & | & |, | Duet With | Featuring | \+ | Feat. | feat. | With | with | X | x | Or ', artist.replace("(", "").replace(")", "").replace("Of The YoungBloodZ", ""))
        self.year = year
        self.releaseYear = 0
        self.genres = []
        self.id = ''
        self.length = 0

        self.danceability = 0
        self.energy = 0
        self.key = 0
        self.loudness = 0
        self.speechiness = 0
        self.acousticness =0
        self.liveness =0
        self.valence = 0
        self.tempo = 0

    def addGenre(self, genre):
            self.genres.append(genre)

    def updateLength(self, time): 
            self.length = time

    def updateID(self, id):
            self.id = id

    def updateReleaseYear(self, year):
        self.releaseYear = year

    def createSpotifyURI(self):
            return f"spotify:track:{track.id}"

    def updateAudioFeatures(self, features):
        self.danceability = features[0]['danceability']
        self.energy = features[0]['energy']
        self.key = features[0]['key']
        self.loudness = features[0]['loudness']
        self.speechiness = features[0]['speechiness']
        self.acousticness = features[0]['acousticness']
        self.liveness = features[0]['liveness']
        self.valence = features[0]['valence']
        self.tempo = features[0]['tempo']


    def __str__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}, id: {self.id}"

    def __repr__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}, id: {self.id}"
