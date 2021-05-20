import ast

from .models import Artist, Track

#format received from https://stackoverflow.com/questions/56768792/how-to-populate-a-manytomany-field-in-django-using-a-csv-file
def write_to_db(file):
    with open(str(file),encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader,None)
        for row in csvreader:
            try:
                track, _ = Track.objects.get_or_create(
                    name = row[0],
                    rank = row[1],
                    year = row[3],
                    spotify_id = row[5],
                    length = row[6],
                    dancebility = row[7],
                    energy = row[8],
                    key = row[9],
                    loudness = row[10],
                    speechiness = row[11],
                    acousticness = row[12],
                    liveness = row[13],
                    valence = row[14],
                    tempo = row[15]
                )
                artist_str = row[2]
                artist_names = ast.literal_eval(artist_str)
                artist_names = list(set(category_names)) # remove duplicates
                for artist_name in artist_names:
                    artist, _ = Artist.objects.get_or_create(name=artist_name)
                    track.artist.add(artist)
            except Exception as e:
                print(e)