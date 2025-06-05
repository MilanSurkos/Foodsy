from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'city',
            'address',
            'postal_code',
            'avatar',
            'preferred_channel'
        ]
        widgets = {
            'preferred_channel': forms.RadioSelect()
        }
