from __future__ import unicode_literals

from django.db import models

# A Movie object specifies the entire movie using various fields.
class Movie(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    producer = models.CharField(max_length=200, null=False, blank=False)
    director_name = models.CharField(max_length=200, null=False, blank=False)
    writer = models.CharField(max_length=200, null=False, blank=False)
    music_by = models.CharField(max_length=200, null=False, blank=False)
    cast = models.CharField(max_length=200, null=False, blank=False) ##### comma seperated value of the starcast as a string
    
    runtime = models.IntegerField(null=False, blank=False) #### in minutes
    release_date = models.DateTimeField(null=False, blank=False)
    budget = models.IntegerField(null=False, blank=False) #### in dollars
    country = models.CharField(max_length=200, null=False, blank=False)
    language = models.CharField(max_length=200, null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)