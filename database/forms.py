from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Create your forms here
class UserSignUP(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']