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
    def form_valid(self, form,*args, **kwargs):
        self.object = form.save(commit=False)
        post_id = self.kwargs['pk']
        unaNoticia = Noticia.objects.get(id=post_id)
        print (unaNoticia)
        self.object.usuario = self.request.user
        self.object.comentarios_post = unaNoticia
        self.object.save()
        return super(ComenCreateview, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        post_id = self.kwargs['pk']
        print(post_id)
        context['post'] = Noticia.objects.filter(id = post_id)
        print(context)
        return context
    #def get_queryset(self, *args, **kwargs):
        #noticia_id = self.kwargs['pk']
        #print(noticia_id)
        #return Noticia.objects.filter(id = noticia_id)
    
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
    
    
class FiltroComentarioList(ListView):
    model = Noticia
    template_name = 'filtroComentario.html'
    def get_queryset(self, *args, **kwargs):
        noticia_id = self.kwargs['pk']
        return comentario_comment.objects.filter(comentarios_post = noticia_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        post_id = self.kwargs['pk']
        print(post_id)
        context['post'] = Noticia.objects.filter(id = post_id)
        return context
        
    
    
   