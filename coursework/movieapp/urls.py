'''Initialsing URL paths'''
from django.urls import path
from django.contrib import admin

from movieapp.views import index, movies_api, movie_api

urlpatterns = [
    path('', index),
    path('api/movies/', movies_api),
    path('api/movies/<int:movie_id>/', movie_api, name="movie_api"),
]
