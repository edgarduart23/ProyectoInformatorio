from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *

app_name = 'categorias'
urlpatterns = [
    path('tipos/', CategoriaList.as_view(), name= 'tipos_categorias'),

]
