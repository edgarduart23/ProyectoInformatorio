"""TrabajoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import detail
from django.views.generic.edit import CreateView

from RepositorioTPFinal.TrabajoFinal.comentarios.views import(
    
    ComenListView,
    ComenDetailView,
    ComenCreateView,
    ComenUpdateView,
    ComenDeleteView
    
    )    
        


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.ProyectoWeb.urls')),
    path('Categorias/', include('apps.categorias.urls')),
    path('', include('apps.Usuarios.urls')),
    
    path(''               ,ComenListView.as_view(),   name=  'list'   ),
    path ('<slug>/'       ,ComenDetailView.as_view(), name=  'detail' ),
    path('create/'        ,ComenCreateView.as_view(), name=  'create' ),
    path('<slug>/update/' ,ComenUpdateView.as_view(), name=  'update' ),
    path('<slug>/delte/'  ,ComenDeleteView.as_view(), name=  'delete' )

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


