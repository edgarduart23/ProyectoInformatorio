from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.
class CategoriaList(ListView):
    model = Categoria
    template_name = 'tipos.html'



    
#class CategoriaCreateView(CreateView):
#    model = Noticia
#    form_class = NoticiaForm
#    template_name = 'createNoticia.html'
#    success_url = reverse_lazy('ProyectoWeb:noticia_list')



#def Tipos(request):
#    return render(request, 'tipos.html')
