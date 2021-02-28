from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class NoticiasList(ListView):
    queryset = Noticia.objects.order_by('-created_date')
    model = Noticia
    template_name = 'noticias.html'
    
class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'createNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'view_type': 'create'
        })
        return context

class NoticiaUpdateView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'updateNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'view_type': 'update'
        })
        return context

   
def PruebaIndex(request):
    return render(request, 'index.html')

class FiltroList(ListView):
    model = Noticia
    template_name = 'filtro.html'

    def get_queryset(self, *args, **kwargs):
        categoria_id = self.kwargs['pk']
        return Noticia.objects.filter(category = categoria_id)
        print(categoria_id)
        pass


