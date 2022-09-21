from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class WatchListItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()

    