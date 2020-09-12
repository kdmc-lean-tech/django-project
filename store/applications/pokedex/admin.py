from django.contrib import admin
from .models import Pokemon, Abilities, Statistics, Type, Category, ImagePokemon
# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Abilities)
admin.site.register(Statistics)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(ImagePokemon)
