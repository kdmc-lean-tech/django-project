from django.urls import path
from .views import (
    getPokemons,
    createPokemon,
    getAbilities,
    createAbility,
    getUpdateAndDeletePokemon,
    getUpdateAndDeleteAbility,
    getCategories,
    createCategory,
    getUpdateAndDeleteCategory,
    getTypes,
    createType,
    getUpdateAndDeleteType
)

urlpatterns = [
    path('pokemons', getPokemons),
    path('pokemon', createPokemon),
    path('pokemon/<pk>', getUpdateAndDeletePokemon),
    path('abilities', getAbilities),
    path('ability', createAbility),
    path('ability/<pk>', getUpdateAndDeleteAbility),
    path('categories', getCategories),
    path('category', createCategory),
    path('category/<pk>', getUpdateAndDeleteCategory),
    path('types', getTypes),
    path('type', createType),
    path('type/<pk>', getUpdateAndDeleteType)
]
