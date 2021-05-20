import ast
import tkinter as tk
import csv
from tkinter import filedialog

from .models import Artist, Track

#format received from https://stackoverflow.com/questions/56768792/how-to-populate-a-manytomany-field-in-django-using-a-csv-file
def write_to_db(file):
    with open(str(file),encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader,None)
        for row in csvreader:
            try:
                track, _ = Track.objects.get_or_create(
                    track_name = row[0],
                    rank = row[1],
                    year = row[3],
                    spotify_id = row[4],
                    length = row[5],
                    danceability = row[6],
                    energy = row[7],
                    music_key = row[8],
                    loudness = row[9],
                    speechiness = row[10],
                    acousticness = row[11],
                    liveness = row[12],
                    valence = row[13],
                    tempo = row[14]
                )

                artist_str = row[2]
                artist_names = ast.literal_eval(artist_str)
                artist_names = list(set(artist_names)) # remove duplicates
                for artist_name in artist_names:
                    artist, _ = Artist.objects.get_or_create(name=artist_name)
                    track.artist.add(artist)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    write_to_db(filename)
    