from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie.views import *

urlpatterns = patterns('',
    
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'(?P<movie_id>[\w\d]+)/update/$', update_movie, name='update_movie'),
    url(r'(?P<movie_id>[\w\d]+)/delete/$', delete_movie, name='delete_movie'),
    url(r'(?P<movie_id>[\w\d]+)/get/$', get_movie, name='get_movie'),
    url(r'add/$', add_movie, name='add_movie'),
    url(r'$', get_movies, name='get_movies'),
    
    
)