from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ProyectoWeb'
urlpatterns = [
       path('noticias/', NoticiasList.as_view(), name= 'noticia_list'),
       path('noticias/add', NoticiaCreateView.as_view(), name= 'noticia_create'),
       path('noticias/edit/<int:pk>/', NoticiaUpdateView.as_view(), name= 'noticia_update'),
       path('prueba/', views.PruebaIndex),
       path('', views.PruebaIndex),
       path('filtro/<int:pk>/', FiltroList.as_view(), name = 'filtro_noticia'),
       path('noticias/my_posts', NoticiaMyPostsView.as_view(), name= 'noticia_myposts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







