from django.db import models
"""
    create TABLE IF NOT EXISTS Tracks (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        title VARCHAR(70), 
        chart_year YEAR(4),
        length DECIMAL(7, 3), 
        dancebility DECIMAL(5, 3), 
        energy DECIMAL(5, 3), 
        liveness DECIMAL(5, 3), 
        loudness DECIMAL(6, 3), 
        speechiness DECIMAL (5, 3), 
        tempo DECIMAL (7, 3), 
        music_key INT, 
        valence DECIMAL(5, 3)
    )
    """
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

class Track(models.Model):
    track_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    spotify_id = models.CharField(max_length=25)
    length = models.DecimalField(max_digits=7, decimal_places=2)
    dancibility = models.DecimalField(max_digits=7, decimal_places=2)
    energy = models.DecimalField(max_digits=7, decimal_places=2)
    loudness = models.DecimalField(max_digits=7, decimal_places=2)
    speechiness = models.DecimalField(max_digits=7, decimal_places=2)
    tempo = models.DecimalField(max_digits=7, decimal_places=2)
    valence = models.DecimalField(max_digits=7, decimal_places=2)
    music_key = models.PositiveSmallIntegerField(blank=True, null=True)
    artist = models.ManyToManyField(Artist)

