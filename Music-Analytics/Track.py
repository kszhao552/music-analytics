import re

class Track:
    def __init__ (self, rank, name, artist, year):
        self.name = name
        self.rank = rank
        self.artist = re.split(', | & | Featuring | featuring | With | with', artist)
        self.year = year
        self.genres = []
        self.length = 0
        self.id = 0


    def addGenre(genre):
            self.genres.append(genre)

    def updateLength(time): 
            self.length = time

    def updateID(id):
            self.id = id

    def createSpotifyURI(self):
            return f"spotify:track:{track.id}"

    def __str__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}"

    def __repr__(self):
            return f"{self.year} rank {self.rank}: {self.name} - {self.artist}: length: {self.length}"
