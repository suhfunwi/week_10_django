from django.shortcuts import render
from .models import Place

def place_list(request):
    places = Place.objects.filter(visited=False).order_by('name')
    return render(request, 'travel_wishlist/wishlist.html', {'places': places})
# Create your views here.
