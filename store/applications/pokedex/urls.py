from django.urls import path
from .views import getPokemons

urlpatterns = [
    path('pokemons', getPokemons),
]
