from django.db import models

class Album(models.Model):
    title = models.TextField()
    artist_name = models.TextField()

class Song(models.Model):
    title = models.TextField()
    seconds = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

