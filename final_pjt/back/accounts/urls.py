from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_pk>/', views.follow),
    path('yourpage/<int:user_pk>/', views.yourpage),
    path('mypage/<int:user_pk>/', views.mypage),
    path('store_score/', views.store_score),
]
