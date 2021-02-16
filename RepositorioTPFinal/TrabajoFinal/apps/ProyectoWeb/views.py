from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from RepositorioTPFinal.TrabajoFinal.apps.ProyectoWeb.models import Noticia

class NoticiasList(ListView):
    model = Noticia
    template_name = 'noticias.html'