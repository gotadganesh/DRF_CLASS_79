from django.shortcuts import render
from myappone.models import Movie
from django.http import HttpResponse,JsonResponse

# Create your views here.

# --------------------------------------------------------------------------------------------
def movie_list(request):
    movies = Movie.objects.all()
    
    data = {
        'movies':list(movies.values()),
        'description': movie.description,
        'active': movie.active
    }
    
    return JsonResponse(data)