from django.urls import path
from RepositorioTPFinal.TrabajoFinal.apps.ProyectoWeb.views import *

app_name = 'ProyectoWeb'
urlpatterns = [
   
    path('noticias/', NoticiasList.as_view()),
]







