# Generated by Django 3.1.6 on 2021-02-23 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('ProyectoWeb', '0003_auto_20210220_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categoria'),
        ),
    ]