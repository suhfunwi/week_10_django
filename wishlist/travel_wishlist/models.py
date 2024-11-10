from django.db import models
from select import select


class Place(models.Model):
    name = models.CharField(max_length=200)
    # the fields that map to the columns in the Place database
    visited = models.BooleanField(default=False)
    # assuming that if the user enters a place, they haven't been there yet

    def __str__(self):
        return f'{self.name} visited? {self.visited}'
# string method in the class that says whether the  user has visited a place or not
# not visible to user, just developer
# Create your models here.
