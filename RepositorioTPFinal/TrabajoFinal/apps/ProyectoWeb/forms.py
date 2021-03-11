from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import SelectDateWidget

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        exclude = ( 'author','created_date', 'published_dates')
        
        #fields = '__all__'

class FormularioFecha(forms.Form):
    Fecha = forms.DateField(widget= SelectDateWidget(), initial=timezone.now())
        