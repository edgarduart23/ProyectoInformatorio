from django.db import models


from django.db import models
from django.utils import timezone



class Noticia(models.Model):
    category = models.ForeignKey('categorias.Categoria', on_delete=models.SET_NULL, blank=False, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="noticias")
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title