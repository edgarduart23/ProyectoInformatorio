# Generated by Django 3.1.6 on 2021-02-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWeb', '0002_noticia_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.ImageField(upload_to='noticias', verbose_name='Imagen'),
        ),
    ]
