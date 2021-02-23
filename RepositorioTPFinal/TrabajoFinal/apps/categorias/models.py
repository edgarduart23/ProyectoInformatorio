from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    



