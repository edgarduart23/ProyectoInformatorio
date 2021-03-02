from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import get_user_model
from django.db import models
from django.utils import timezone

#User = get_user_model()


class Noticia(models.Model):
    category = models.ForeignKey('categorias.Categoria', on_delete=models.SET_NULL, blank=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_dates = models.DateTimeField(default=timezone.now)
    image = models.ImageField(verbose_name="Imagen", upload_to="noticias")

    def __str__(self):
        return self.title
<<<<<<< HEAD
        
=======
    
    def get_absolute_url(self):
        return reverse('noticia-update', kwargs={'pk': self.pk})
>>>>>>> desarrollo
