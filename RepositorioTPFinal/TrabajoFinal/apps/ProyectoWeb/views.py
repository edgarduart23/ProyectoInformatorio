from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class NoticiasList(ListView):
    model = Noticia
    template_name = 'noticias.html'
    
class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'createNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    
def PruebaIndex(request):
    return render(request, 'index.html')
