from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField ( max_length=63, label='',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=63,label='',widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailField(),
            'last_name': forms.TextInput(attrs={'placeholder': 'Votre postNom '}),
        }