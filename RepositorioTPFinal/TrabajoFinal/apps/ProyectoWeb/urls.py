from django.urls import path
from apps.ProyectoWeb.views import *

app_name = 'ProyectoWeb'
urlpatterns = [
       path('noticias/', NoticiasList.as_view()),
]







