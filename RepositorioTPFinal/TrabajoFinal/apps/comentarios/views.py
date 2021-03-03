#from apps.comentarios.models import comentario_comment
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  apps.comentarios.models import comentario_comment, vistacomentario_postview, megusta_like
from .forms import *
from django.urls import reverse_lazy


class ComenListView(ListView):
   
    model = comentario_comment
    template_name = 'comentario_list.html'

class ComenDetailView(DetailView):
    model = comentario_comment
    
class ComenCreateview(CreateView):
    model = comentario_comment
    form_class = ComentarioForm
    template_name = 'comentarios_create.html'
    success_url = reverse_lazy('comentarios:comment_list')
    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(ComenCreateview, self).form_valid(form)
    
class ComenUpdateView(UpdateView):
    model = comentario_comment
    fields= (
        'category' ,
        'author',
        'title',
        'text' ,
        'created_date' ,
        'image'
    )
    
class ComenDeleteView(DeleteView):
    model = comentario_comment
    success_url = '/'
    
    
        
    
    
   