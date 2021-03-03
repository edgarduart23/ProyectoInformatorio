from ProyectoInformatorio.RepositorioTPFinal.TrabajoFinal.apps.comentarios.models import comentario_comment
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  .models import comentario_comment, vistacomentario_postview, megusta_like




class ComenListView(ListView):
     model = comentario_comment
     

class ComenDetailView(DetailView):
    model = comentario_comment
    
class ComenCreateview(CreateView):
    model = comentario_comment
    
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
    
    
        
    
    
   