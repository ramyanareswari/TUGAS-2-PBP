from django.db import models

# Create your models here.
class WatchListItem(models.Model):
    watched = models.BooleanField(default=True)
    title = models.TextField(default='')
    rating = models.FloatField(default=0)
    release_date = models.DateField()
    review = models.TextField(default='')

