from django import forms
from .models import Identity


class IdentityForm(forms.ModelForm):
    class Meta:
        model = Identity
        fields = ['user','firstName','lastName','photo', 'description','address' , 'country','dateOfBirth ',' eyeColor','nft_token_id']
