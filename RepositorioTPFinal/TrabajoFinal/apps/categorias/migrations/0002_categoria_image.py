# Generated by Django 3.1.6 on 2021-02-27 18:14
# Generated by Django 3.1.6 on 2021-02-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='image',
            field=models.ImageField(default=2, upload_to='categorias'),
            preserve_default=False,
        ),
    ]