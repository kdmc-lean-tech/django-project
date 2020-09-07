from django.urls import path
from .views import getCharacters, createCharacter, getUpdateOrDeleteCharacter, getPowers

urlpatterns = [
    path('characters', getCharacters),
    path('character', createCharacter),
    path('character/<pk>', getUpdateOrDeleteCharacter),
    path('powers', getPowers)
]
