from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Uživatelské jméno'
        self.fields['username'].help_text = 'Povinné. Maximálně 150 znaků. Používejte pouze písmena, číslice a znaky @/./+/-/_.'
        self.fields['email'].label = 'E-mail'
        self.fields['email'].help_text = 'Zadejte platný e-mail.'
        self.fields['password1'].label = 'Heslo'
        self.fields['password1'].help_text = 'Vaše heslo musí obsahovat alespoň 8 znaků a nesmí být příliš jednoduché.'
        self.fields['password2'].label = 'Potvrzení hesla'
        self.fields['password2'].help_text = 'Zadejte stejné heslo pro ověření.'
        self.fields['city'].label = 'Město'
        self.fields['address'].label = 'Adresa'
        self.fields['postal_code'].label = 'PSČ'
        self.fields['avatar'].label = 'Profilová fotka'
        self.fields['preferred_channel'].label = 'Preferovaný způsob kontaktu'

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
