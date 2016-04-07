from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from bson.json_util import dumps
from movie.models import Movie
from datetime import datetime
import json

def get_movies(request):
    """
    GET: /api/movies/
    get list of all movie objects with all their fields
    """
    movie_objs = Movie.objects.all().values("id", "name", 
        "producer", "director_name", "writer", "music_by", 
        "cast", "runtime", "release_date", "budget", "country", 
        "language")

    if movie_objs.count() == 0:
        movie_objs = {}
    
    data = dumps(movie_objs)

    try:
        return HttpResponse(data, 
                content_type="application/json", status=200)
    except:
        return HttpResponse(json.dumps({"status": "unsuccessful"}),
                content_type="application/json", status=200)

def get_movie(request, movie_id=None):
    """
    GET: /api/movies/pk-id/get/
    get movie objects with all its fields pertaining to the 
    id specified in the url
    """
    if request.method == "GET":
            
        if movie_id is not None:
            movie_obj = []
            try:
                ########## Fetches a single Movie object ##########3
                movie_obj = Movie.objects.filter(id=int(movie_id)).values("id", "name", 
                    "producer", "director_name", "writer", "music_by", 
                    "cast", "runtime", "release_date", "budget", "country", 
                    "language")
                data =  dumps(movie_obj)

                return HttpResponse(data,
                    content_type="application/json", status=200)

            except Exception,e:
                print e
                return HttpResponse(json.dumps({"status": "unsuccessful"}), 
                    content_type="application/json", status=404)

    return HttpResponse(json.dumps({"status": "unsuccessful"}), 
        content_type="application/json", status=404)

@csrf_exempt
def add_movie(request):
    """
    POST: /api/movies/add/
    Specify the name ,producer, director_name, music_by, writer, cast,
    release_date, runtime, budget, country, language
    cast: comma seperated value of the star cast
    release_date: date specified in dd-mm-yyyy format
    runtime: in minutes
    budget: in dollars/inr
    """
    if request.method == "POST":
        
        movie_id = ""
        movie = Movie()
        try:
            movie.name = request.POST.get("name",)
            movie.producer = request.POST.get("producer")
            movie.director_name = request.POST.get("director_name")
            movie.writer = request.POST.get("writer")
            movie.music_by = request.POST.get("music_by")
            movie.cast = request.POST.get("cast")

            movie.release_date = datetime.strptime(request.POST.get("release_date"), '%d-%m-%Y')

            movie.runtime = int(request.POST.get("runtime"))
            movie.budget = int(request.POST.get("budget"))
            movie.country = request.POST.get("country")
            movie.language = request.POST.get("language")

            movie.save()
        except Exception,e:
            print e
            ####### Missing request parameters ###########
            response =  HttpResponse(json.dumps({"status": "unsuccessful"}), 
                content_type="application/json", status=404)
            response['Access-Control-Allow-Origin'] = '*'
            return response

        response = HttpResponse(json.dumps({"id": movie.id}), 
            content_type="application/json", status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    else:
        response = HttpResponse(json.dumps({"status": "unsuccessful"}), 
            content_type="application/json", status=400)
        response['Access-Control-Allow-Origin'] = '*'
        return response

@csrf_exempt
def update_movie(request, movie_id=None):
    pass

def delete_movie(request, movie_id=None):
    """
    GET: /api/movies/pk-id/delete/
    delete movie objects pertaining to the 
    id specified in the url
    """

    provider = ""
    try:
        movie_obj = Movie.objects.get(id=movie_id).delete()
        
        return HttpResponse(json.dumps({"deleted": 1}), 
            content_type="application/json", status=200)
    except:
        return HttpResponse(json.dumps({"status": "unsuccessful"}),
            content_type="application/json", status=404)
