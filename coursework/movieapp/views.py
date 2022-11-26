from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from movieapp.models import Movie
from django.shortcuts import get_object_or_404
import json


def index(request: HttpRequest) -> HttpResponse:
    '''Index shows a welcome message on the backend home page'''
    heading = "Welcome to my Movie App!"
    return render(request, "movieapp/index.html", {
        'heading': heading,
        'n': Movie.objects.all().count()
    })


def movies_api(request):
    '''This function handles the GET and POST AJAX request methods.
    The GET method fetches all of the movies in the database.
    '''
    if request.method == 'GET':
        return JsonResponse({
            'movies': [
                movie.to_dict()
                for movie in Movie.objects.all()
            ]
        })

    '''The POST method adds a new movie to the database.'''
    if request.method == 'POST':
        data = json.load(request)
        title = data.get('title')
        date_released = data.get('date_released')
        rating = data.get('rating')
        award_winning = data.get('award_winning')
        movie = Movie.objects.create(
            title=title,
            date_released=date_released,
            rating=rating,
            award_winning=award_winning,
        )
        return JsonResponse(movie.to_dict())
    else:
        return HttpResponseBadRequest("Bad Request")


def movie_api(request: HttpRequest, movie_id: int) -> HttpResponse:
    '''This function allows each movie to appear individually
    on a page on the backend, defined by their ID.
    It is also where the PUT and DELETE methods are held.
    '''
    movie = get_object_or_404(Movie, id=movie_id)
    '''This GET method fetches one movie/element from the database.'''
    if request.method == 'GET':
        return JsonResponse(movie.to_dict())
    '''The DELETE method deletes a movie from the database.'''
    if request.method == 'DELETE':
        movie.delete()
        return JsonResponse({})
    '''The PUT method updates a movie in the database.'''
    if request.method == 'PUT':
        data = json.load(request)
        movie.title = data.get('title')
        movie.date_released = data.get('date_released')
        movie.rating = data.get('rating')
        movie.award_winning = data.get('award_winning')
        movie.save(update_fields=['title'])
        movie.save(update_fields=['date_released'])
        movie.save(update_fields=['rating'])
        movie.save(update_fields=['award_winning'])
        return JsonResponse(movie.to_dict())
    return HttpResponse
