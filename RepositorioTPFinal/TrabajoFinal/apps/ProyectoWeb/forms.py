from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        exclude = ('created_date', 'published_dates')
        #fields = '__all__'
