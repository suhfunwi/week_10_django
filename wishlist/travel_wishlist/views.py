from django.shortcuts import render
from .models import Place

def place_list(request):
    places = Place.objects.filter(visited=False).order_by('name')
    # fetches objects that meet the filter requirements and
    # places them in a list called places and ordering them by name
    return render(request, 'travel_wishlist/wishlist.html', {'places': places})
# function is called by django and given info about
# the request the browser is making
# Create your views here.
