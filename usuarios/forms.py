from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasena', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
