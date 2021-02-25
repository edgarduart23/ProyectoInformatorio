from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ProyectoWeb'
urlpatterns = [
       path('noticias/', NoticiasList.as_view(), name= 'noticia_list'),
       path('noticias/add', NoticiaCreateView.as_view(), name= 'noticia_create'),
<<<<<<< HEAD
       path('', views.PruebaIndex)
=======
       path('prueba/', views.PruebaIndex),
>>>>>>> ba5bba17ee3b105ae96f76195750f15795f5735a
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







