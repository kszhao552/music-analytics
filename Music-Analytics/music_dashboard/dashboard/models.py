from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta(object):
        ordering = ['name']

class Track(models.Model):
    track_name = models.CharField(max_length=100)
    rank = models.PositiveSmallIntegerField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    spotify_id = models.CharField(max_length=25)
    length = models.DecimalField(max_digits=7, decimal_places=3)
    danceability = models.DecimalField(max_digits=7, decimal_places=3)
    energy = models.DecimalField(max_digits=7, decimal_places=3)
    loudness = models.DecimalField(max_digits=7, decimal_places=3)
    speechiness = models.DecimalField(max_digits=7, decimal_places=3)
    tempo = models.DecimalField(max_digits=7, decimal_places=3)
    valence = models.DecimalField(max_digits=7, decimal_places=3)
    music_key = models.PositiveSmallIntegerField(blank=True, null=True)
    acousticness = models.DecimalField(max_digits=7, decimal_places=3)
    liveness = models.DecimalField(max_digits=7, decimal_places=3)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.track_name
    class Meta(object):
        ordering = ['track_name', 'year']
