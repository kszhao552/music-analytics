import re
import spotipy
import spotipy.oauth2 as oauth2

class Track:
    def __init__ (self, rank, name, artist, year):
        self.name = name
        self.rank = rank
        self.artist = re.split(', | & | Featuring | featuring | With | with', artist)
        self.year = year
        self.genres = []
        self.id = ''
        self.length = 0

    def addGenre(self, genre):
            self.genres.append(genre)

    def updateLength(self, time): 
            self.length = time

    def updateID(self, id):
            self.id = id

    def createSpotifyURI(self):
            return f"spotify:track:{track.id}"

    def __str__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}, id: {self.id}"

    def __repr__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}, id: {self.id}"
