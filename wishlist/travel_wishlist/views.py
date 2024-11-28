from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, TripReviewForm
from django.contrib.auth.decorators import login_required
# django has a built in login import
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
# type this in before every view to require a login for that view

def place_list(request):

    if request.method == 'POST': #create new place
        form = NewPlaceForm(request.POST)
        # make a form from data in the request
        place = form.save(commit=False)
        # creates new model object from form
        place.user = request.user
        if form.is_valid():
            # validation against db constraints
            place.save()
        #     saves place to db
        return redirect('place_list')
    #     reloads the home page


    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    # fetches objects that meet the filter requirements and
    # places them in a list called places and ordering them by name
    # further filters it by the user making the request
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})
# render takes the template, list of places, and the form and make a webpage with all those
# function is called by django and given info about
# the request the browser is making
# Create your views here.

@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

@login_required
def place_was_visited(request, place_pk):
    #place_pk will extract the int from the path
    if request.method == 'POST':
        place = get_object_or_404(Place, pk = place_pk)
        #makes query to db, if the object isn't found it returns a 404 error
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden
        # if the wrong user is trying to make changes
        # on the wishlist, it will be forbidden
        # place = Place.objects.get(pk = place_pk)
    #     db query that gets the matching pk object
        place.visited = True
        place.save()

    return redirect('place_list')
    # return redirect('places_visited')

# returns you to the name of that path

@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk= place_pk)
    if place.user != request.user:
        return HttpResponseForbidden
    # if someone other than the user tries
    # to make changes it will be forbidden
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance=place)
    #     new TRF object from the data sent with the http request, and put in
    #     data the user sent and use it to update a model instance from the DB
        if form.is_valid():
            form.save()
    #         updates the place object with the data provided
            messages.info(request, 'Trip information updated')
    #         shows a temporary message to the user
        else:
            messages.error(request, form.errors)
            return redirect('place_details', place_pk=place_pk)
    #     updating place_details and redirecting to the same place

    else:
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/place_detail.html', {'place': place, 'review_form': review_form})
        else:
            return render(request, 'travel_wishlist/place_detail.html', {'place': place})
    #     only displays the review form if the place is visited



    return render(request, 'travel_wishlist/place_detail.html', {'place': place})

@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk= place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden
#     function to delete a place

@login_required
def about(request):
    author = 'Suh'
    about =  ' A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})