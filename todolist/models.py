from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)