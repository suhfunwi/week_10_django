from django.shortcuts import render, redirect, get_object_or_404

from .models import Place
from .forms import NewPlaceForm

def place_list(request):

    if request.method == 'POST': #create new place
        form = NewPlaceForm(request.POST)
        # make a form from data in the request
        place = form.save()
        # creates new model object from form
        if form.is_valid():
            # validation against db constraints
            place.save()
        #     saves place to db
        return redirect('place_list')
    #     reloads the home page


    places = Place.objects.filter(visited=False).order_by('name')
    # fetches objects that meet the filter requirements and
    # places them in a list called places and ordering them by name
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})
# render takes the template, list of places, and the form and make a webpage with all those
# function is called by django and given info about
# the request the browser is making
# Create your views here.

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def place_was_visited(request, place_pk):
    #place_pk will extract the int from the path
    if request.method == 'POST':
        place = get_object_or_404(Place, pk = place_pk)
        #makes query to db, if the object isn't found it returns a 404 error
        # place = Place.objects.get(pk = place_pk)
    #     db query that gets the matching pk object
        place.visited = True
        place.save()

    return redirect('place_list')
    # return redirect('places_visited')

# returns you to the name of that path




def about(request):
    author = 'Suh'
    about =  ' A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})