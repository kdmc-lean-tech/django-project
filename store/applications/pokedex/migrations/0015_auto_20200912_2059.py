# Generated by Django 3.1.1 on 2020-09-13 01:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0014_auto_20200911_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepokemon',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='file'),
        ),
    ]
