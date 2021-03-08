from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ProyectoWeb'
urlpatterns = [
       path('', NoticiasList.as_view(), name= 'noticia_list'),
       path('noticias/add', NoticiaCreateView.as_view(), name= 'noticia_create'),
       path('noticias/detail/<int:pk>', NoticiaDetailView.as_view(), name= 'noticia_detail'),
       path('noticias/edit/<int:pk>/', NoticiaUpdateView.as_view(), name= 'noticia_update'),
       path('noticias/delete/<int:pk>/', NoticiaDeleteView.as_view(), name= 'noticia_delete'),

       path('filtro/<int:pk>/', FiltroList.as_view(), name = 'filtro_noticia'),
       path('ordenar/', OrdenarList.as_view(), name = 'ordenar_noticia'),
       path('noticias/my_posts', NoticiaMyPostsView.as_view(), name= 'noticia_myposts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







