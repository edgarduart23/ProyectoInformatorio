from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *

app_name = 'comentarios'
urlpatterns = [
    path('comentarios'               ,ComenListView.as_view(),   name=  'comment_list'   ),
    path ('comentarios/detail/<int:pk>'       ,ComenDetailView.as_view(), name=  'comment_detail' ),
    path('comentarios/create/<int:pk>'        ,ComenCreateview.as_view(), name=  'comment_create' ),
    path('comentarios/update/<int:pk>' ,ComenUpdateView.as_view(), name=  'comment_update' ),
    path('comentarios/delete/<int:pk>'  ,ComenDeleteView.as_view(), name=  'comment_delete' )
    

]

    