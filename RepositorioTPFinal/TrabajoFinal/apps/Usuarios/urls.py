from django.urls import path
from .views import register
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'Usuarios'
urlpatterns = [
       path('registro/', views.register, name = 'registro'),
       path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
       path('logout/', LogoutView.as_view(template_name ='logout.html'), name = 'logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
