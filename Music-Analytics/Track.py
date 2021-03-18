class Track:
    def __init__ (self, rank, name, artist):
        self.name = name
        self.rank = rank
        self.artist = artist
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
