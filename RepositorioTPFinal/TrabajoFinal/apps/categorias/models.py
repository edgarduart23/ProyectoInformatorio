from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to = 'categorias')
   

    def __str__(self):
        return self.name
    



