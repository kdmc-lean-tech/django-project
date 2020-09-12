from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Type, Abilities, Category, Pokemon, Statistics, ImagePokemon


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name', 'description')


class AbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abilities
        fields = ('id', 'name', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class PokemonSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    type = TypeSerializer(many=True)
    debilities = TypeSerializer(many=True)
    abilities = AbilitiesSerializer(read_only=True)

    class Meta:
        model = Pokemon
        fields = (
            'id',
            'name',
            'weight',
            'sex',
            'height',
            'description',
            'type',
            'abilities',
            'previousEvolution',
            'laterEvolution',
            'category',
            'debilities'
        )


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = (
            'id',
            'pokemon',
            'ps',
            'attack',
            'defense',
            'specialAttack',
            'specialDefense',
            'speed'
        )


class ImagePokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePokemon
        fields = (
            'id',
            'pokemon',
            'urlImage',
            'keyImage'
        )

