from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Comment
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, BasketSerializer
from .forms import  CommentForm, AnswerForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
import random, json

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
@api_view(['GET'])
def search(request, inputdata):
    if request.method == 'GET':
        movies = Movie.objects.filter(Q(title__icontains=inputdata) | Q(overview__icontains=inputdata))
        # serializer = MovieListSerializer(movies, many=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
@api_view(['GET'])
def recommend(request, genre1, genre2):
    if request.method == 'GET':
        movies = Movie.objects.filter(Q(genre_ids__icontains=genre1) & Q(genre_ids__icontains=genre2))
        # serializer = MovieListSerializer(movies, many=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
    
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
    
@api_view(['GET', 'POST'])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            user = request.user
            user.point += 10
            user.save()
            # return Response(status=status.HTTP_201_CREATED)
    
    comments = Comment.objects.filter(movie=movie_pk)
    serializer = CommentSerializer(comments, many=True)
    
    
    return Response(serializer.data)


@api_view(['POST'])
def push_basket(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # if request.user.is_authenticated():
    if movie.basket_users.filter(pk=request.user.pk).exists():
        movie.basket_users.remove(request.user)
    else: 
        movie.basket_users.add(request.user)
    
    serializer = MovieSerializer(movie)

    return Response(serializer.data)


@api_view(['POST'])
def like_comment(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    serializer = CommentSerializer(comment)
    
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_comment(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)


# 재만 수정 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@api_view(['GET'])     
def get_basket(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    movies = person.basket_movies
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bring_movie(request):
    movies = Movie.objects.all()
    random_movie = random.choice(movies)
    movie_title = random_movie.title.replace(' ', '')
    data = {
        'moviePk' : random_movie.id,
        'poster_path' : random_movie.poster_path
    }

    return JsonResponse(data)


@api_view(['POST'])
def send_answer(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie_title = movie.title.replace(' ', '')
    data = request.POST['answer']
    if data in  movie_title and len(data) >= len( movie_title) / 3:
        serializer = {
            'success' : True,
            'content' : '성공!',
            'point' : 500
        }
        return JsonResponse(serializer)
    else:
        serializer = {
            'success' : False,
            'content' : '실패!',
            'point' : -100,
            'answer' : movie_title
        }

        return JsonResponse(serializer)