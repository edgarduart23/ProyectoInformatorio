from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('ProyectoWeb:noticia_list')
    else:
        form = UserRegisterForm()
    
    ctx = {'form' : form}
    return render(request, 'register.html', ctx)    
    
def PruebaIndex(request):
    return render(request, 'index.html')
