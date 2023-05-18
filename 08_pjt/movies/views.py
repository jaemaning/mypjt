from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from django.contrib.auth import get_user_model
from .models import Genre, Movie

# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    context = {
        "movies": movies
    }
    return render(request, "movies/index.html", context)
    
@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    data = []
    
    for genre in genres:
        genre_pk = genre.pk
        gen = get_object_or_404(Genre, pk=genre_pk)
        data.append(gen.name)
    result = ", ".join(data)
    
    context = {
        "movie": movie,
        "data": result
    }
    return render(request, 'movies/detail.html', context)

@require_safe
def recommended(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    print(person.favorite_genre.name)
    recommended_movies = set()
    movies = get_list_or_404(Movie)
    for movie in movies:
        for genre in movie.genres.all():
            if genre.name == person.favorite_genre.name:
                recommended_movies.add((movie, movie.vote_average))
    
    recommended_movies = sorted(list(recommended_movies), key=lambda x: x[1], reverse=True)[:10]

    context = {
        "person": person,
        "recommended_movies": recommended_movies
    }
    return render(request, 'movies/recommended.html', context)