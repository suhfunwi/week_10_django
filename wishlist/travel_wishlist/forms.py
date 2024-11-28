from django import forms
from django.forms import FileInput, DateInput
from .models import Place

class NewPlaceForm(forms.ModelForm):
    # ModelForm is a form for the webpage that is related to the model
    class Meta:
        model = Place
        fields = ('name', 'visited')
        # the fields we want to display on the form

class DateInput(forms.DateInput):
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }
        # new form for trip review