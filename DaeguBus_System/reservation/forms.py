import imp
from django import forms
from reservation.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'type']