from django.forms import ModelForm
from .models import *

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'