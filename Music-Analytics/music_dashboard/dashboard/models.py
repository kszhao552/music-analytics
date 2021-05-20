from django.db import models

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

