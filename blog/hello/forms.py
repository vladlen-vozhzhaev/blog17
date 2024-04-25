from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
        }