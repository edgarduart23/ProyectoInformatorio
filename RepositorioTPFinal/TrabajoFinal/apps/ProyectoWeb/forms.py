from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
