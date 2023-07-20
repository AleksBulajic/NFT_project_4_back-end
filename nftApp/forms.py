# Import the necessary modules from Django
from django import forms
from .models import Identity

# Define a form class named IdentityForm that inherits from forms.ModelForm
class IdentityForm(forms.ModelForm):
    # The Meta class contains additional information about the form
    class Meta:
        # The model attribute specifies the model that the form is based on
        model = Identity
        # The fields attribute specifies which fields from the model should be included in the form
        fields = ['user', 'firstName', 'lastName', 'photo', 'description', 'address', 'country', 'dateOfBirth', 'eyeColor']
        # Each field specified in the 'fields' list will be included in the form and will have corresponding form widgets generated automatically by Django


