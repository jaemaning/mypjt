from django.db import models
import json

# Create your models here.
from django.db import models
from django.conf import settings

class Movie(models.Model):
    adult = models.BooleanField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    overview = models.TextField(blank=True)
    release_date = models.DateTimeField(blank=True)
    poster_path = models.TextField(blank=True)
    backdrop_path = models.TextField(blank=True)
    vote_count = models.IntegerField(blank=True)
    vote_average = models.FloatField(blank=True)
    popularity = models.FloatField(blank=True)
    video = models.BooleanField(blank=True)
    genre_ids = models.TextField(blank=True)
    basket_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='basket_movies')
    video_id = models.TextField(blank=True)
    # def set_genres_id(self, value):
    #     self.genres_id = json.dumps(value)
    # actors = models.ManyToManyField(Actor, related_name="movies")

class Comment(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.IntegerField(default=0)
      