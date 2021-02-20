from django.urls import path
from apps.ProyectoWeb.views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'ProyectoWeb'
urlpatterns = [
       path('noticias/', NoticiasList.as_view()),
       path('prueba/', views.PruebaIndex)
]
##urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







