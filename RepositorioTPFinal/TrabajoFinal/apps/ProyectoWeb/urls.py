from django.urls import path
from RepositorioTPFinal.TrabajoFinal.apps.ProyectoWeb.views import *

app_name = 'ProyectoWeb'
urlpatterns = [
   
    path('noticias/', NoticiasList.as_view()),
]







urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    path('dos/', mysecondview, name='vista2')
]

