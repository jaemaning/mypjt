from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/create_comment/', views.create_comment),
    path('basket/<int:movie_pk>/', views.push_basket),
    path('get_basket/<int:user_pk>/', views.get_basket),
    path('<int:movie_pk>/like_comment/<int:comment_pk>/', views.like_comment),
    path('<int:movie_pk>/delete_comment/<int:comment_pk>/', views.delete_comment),
    path('search/<inputdata>/', views.search),
    path('recommend/<genre1>/<genre2>/', views.recommend),
    path('bring_movie/', views.bring_movie),
    path('send_answer/<int:movie_pk>/', views.send_answer),
]
