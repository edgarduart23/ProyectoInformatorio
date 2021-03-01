from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class NoticiasList(ListView):
    queryset = Noticia.objects.order_by('-created_date')
    model = Noticia
    template_name = 'noticias.html'
    
class NoticiaCreateView(LoginRequiredMixin,CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'createNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    
    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(NoticiaCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        user = self.request.user
        context.update({
            'view_type': 'create',
            'user': 'user'
            
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


