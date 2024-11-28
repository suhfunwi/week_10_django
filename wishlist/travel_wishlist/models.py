from django.core.files.storage import default_storage
from django.db import models
from select import select
from django.contrib.auth.models import User
from django.core.files.storage import default_storage


class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    # sets up the models to use foreign keys, doesn't allow the key to be empty(null),
    # and if the user is deleted then all associated places will be deleted(on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # the fields that map to the columns in the Place database
    visited = models.BooleanField(default=False)
    # assuming that if the user enters a place, they haven't been there yet
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    # allows these fields to be blank
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)
    # lists the directory the images would be uploaded to, but they can also be left blank

    def save(self, *args, **kwargs):
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)
    #if there is an old place and the old place has a photo, and that
    # photo is different than the new photo, then delete the old photo
        super().save(*args, **kwargs)

    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)
            
        super().delete(*args, **kwargs)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        # putting the image in a string method
        notes_str = self.notes[100:] if self.notes else 'no notes'
        # truncates to 100
        return f'{self.name}, visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo: {photo_str}'
# string method in the class that says whether the user has visited a place or not, and lists notes and image if applicable
# not visible to user, just developer
# every individual part of the website is an app
# Create your models here.


# commands to remember
# python manage.py runserver: runs the server
# cd .. : navigates to the parent directory
# venv\Scripts\activate: activates virtual environment
# admin password is password