from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ComentarioForm(ModelForm):
    class Meta:
        model = comentario_comment
        exclude = ( 'usuario','tiempo_comentario_timestamp', 'comentarios_post')
        #fields = '__all__'