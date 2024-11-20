from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    # ModelForm is a form for the webpage that is related to the model
    class Meta:
        model = Place
        fields = ('name', 'visited')
        # the fields we want to display on the form