from django.urls import path
from apps.ProyectoWeb.views import *
from . import views

app_name = 'ProyectoWeb'
urlpatterns = [
       path('noticias/', NoticiasList.as_view()),
       path('prueba/', views.PruebaIndex)
]








