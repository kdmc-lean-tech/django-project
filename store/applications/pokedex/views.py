from django.shortcuts import render
from .models import Pokemon, Statistics, Abilities, Category, Type
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PokemonSerializer, StatisticsSerializer, AbilitiesSerializer, CategorySerializer, TypeSerializer

# Create your views here.

# Pokemon views


@api_view(['GET'])
def getPokemons(request):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Abilities Views


@api_view(['GET'])
def getAbilities(request):
    abilities = Abilities.objects.all()
    serializer = AbilitiesSerializer(abilities, many=True)
    return Response(serializer, status=status.HTTP_200_OK)
