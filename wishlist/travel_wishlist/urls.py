# main routing for the whole app

from django.urls import path, include
from django.contrib import admin
from . import views

# list of urls the app will recognize

urlpatterns = [
    path('', views.place_list, name='place_list'),
# request to the empty string path(homepage) that says any requests
    # made to it should be handled by place_list function in views.py
    path('admin/', admin.site.urls),
    path('', include('travel_wishlist.urls'))
]