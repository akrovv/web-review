from django import forms
from .models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'password1')

class UserForm(forms.ModelForm):
    game_name = forms.CharField()
    hours_played = forms.IntegerField()
    developer = forms.CharField()

    class Meta:
        model = Users
        fields = ['game_name', 'hours_played', 'developer']
