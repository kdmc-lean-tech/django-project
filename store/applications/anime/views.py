from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .auxiliary import errorMessage, sendMessage
from .models import Character, Power
from .serializers import CharacterSerializer, PowerSerializer

# Create your views here.


@api_view(['GET'])
def getCharacters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getPowers(request):
    powers = Power.objects.all()
    serializer = PowerSerializer(powers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createCharacter(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getUpdateOrDeleteCharacter(request, pk):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return HttpResponse(
            errorMessage('The article with id ' + pk + ' no exist'),
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        character.delete()
        return HttpResponse(
            sendMessage('The character with id ' + pk + ' has been deleted'),
            status=status.HTTP_204_NO_CONTENT
        )

