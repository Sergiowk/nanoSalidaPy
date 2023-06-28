#Form to add a new Driver manually into the model
from django import forms

from .models import Drivers


class DriversForm(forms.ModelForm):
    class Meta:
        model=Drivers
        fields=('name', 'number', 'nationality', 'dob', 'comments')



