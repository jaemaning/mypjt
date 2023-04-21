from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET','POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user_id = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = Comment.objects.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'movies/detail.html', context)

@require_POST
@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.pk == pk:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'movie': movie,
            'form': form,
        }
        return render(request, 'movies/update.html', context)
    return redirect('movies:detail', pk)

@require_POST
@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        print(movie)
        comment.movie_id = movie
        comment.user_id = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)

@require_POST
@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user_id:
        comment.delete()
    return redirect("movies:detail", movie_pk)

@require_POST
@login_required
def likes(request, pk):
    movie = Movie.objects.get(pk=pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
    else:
        movie.movie_like_users.add(request.user)
    return redirect('movies:index')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searcheds = list(searched.strip().split())
        movies = set()
        
        for searched in searcheds:
            movies.add(Movie.objects.filter(title__contains=searched))

        context = {
            'movies': list(movies)
        }
        
        return render(request, 'movies/search.html', context)
