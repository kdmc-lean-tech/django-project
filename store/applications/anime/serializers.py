from rest_framework import serializers
from .models import Character, Power


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'age', 'description', 'image']


class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'name', 'description', 'character']

