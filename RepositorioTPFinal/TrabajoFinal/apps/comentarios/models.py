
from apps.ProyectoWeb.models  import Noticia 
from django.db import models
from django.utils import timezone


   
#clase comentario donde definimos lo que se comenta del posteo anteriormente definido
    
class comentario_comment(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comentarios_post            = models.ForeignKey(Noticia,on_delete=models.CASCADE)
    tiempo_comentario_timestamp = models.DateTimeField(default=timezone.now)
    contenido_content           = models.TextField()
    
    def __str__(self): 
         return self.user.username
     
     # hacemos la vista del comentario
     
class vistacomentario_postview(models.Model):
     usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     post = models.ForeignKey(Noticia,on_delete=models.CASCADE)
     tiempoposteo_timestamp = models.DateTimeField(auto_now_add=True)
      
     
     def __str__ (self):
         return self.user.username 
     
     #hacemos los likes del comentario mencionado

class megusta_like(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comentario_post = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username 
    