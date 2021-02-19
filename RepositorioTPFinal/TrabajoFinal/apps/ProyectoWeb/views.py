from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.ProyectoWeb.models import *

class NoticiasList(ListView):
    model = Noticia
    template_name = 'noticias.html'
    
def PruebaIndex(request):
    return render(request, 'index.html')
