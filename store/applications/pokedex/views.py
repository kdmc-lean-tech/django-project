from django.shortcuts import render
from .models import Pokemon, Statistics, Abilities, Category, Type
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import PokemonSerializer, StatisticsSerializer, AbilitiesSerializer, CategorySerializer, TypeSerializer
from .auxiliary import errorMessage, sendMessage
# Create your views here.

# Pokemon views


@api_view(['GET'])
def getPokemons(request):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createPokemon(request):
    serializer = PokemonSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUpdateAndDeletePokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return HttpResponse(
            errorMessage('The pokemon with id ' + pk + ' no exist'),
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Abilities Views


@api_view(['GET'])
def getAbilities(request):
    abilities = Abilities.objects.all()
    serializer = AbilitiesSerializer(abilities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createAbility(request):
    serializer = AbilitiesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getUpdateAndDeleteAbility(request, pk):
    try:
        ability = Abilities.objects.get(pk=pk)
    except Abilities.DoesNotExist:
        return HttpResponse(
            errorMessage('The ability with id ' + pk + ' no exist'),
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = AbilitiesSerializer(ability)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = AbilitiesSerializer(ability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        ability.delete()
        return HttpResponse(
            sendMessage('The ability with id ' + pk + ' has been deleted'),
            status=status.HTTP_204_NO_CONTENT
        )


# Categories Views


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getUpdateAndDeleteCategory(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(
            errorMessage('The category with id ' + pk + ' no exist'),
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        category.delete()
        return HttpResponse(
            sendMessage('The category with id ' + pk + ' has been deleted'),
            status=status.HTTP_204_NO_CONTENT
        )


# Types Views


@api_view(['GET'])
def getTypes(request):
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createType(request):
    serializer = TypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getUpdateAndDeleteType(request, pk):
    try:
        type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
        return HttpResponse(
            errorMessage('The type with id ' + pk + ' no exist'),
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = TypeSerializer(type)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = TypeSerializer(type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        type.delete()
        return HttpResponse(
            sendMessage('The type with id ' + pk + ' has been deleted'),
            status=status.HTTP_204_NO_CONTENT
        )

