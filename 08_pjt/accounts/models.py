from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    favorite_genre = models.ForeignKey("movies.Genre", on_delete=models.CASCADE)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
