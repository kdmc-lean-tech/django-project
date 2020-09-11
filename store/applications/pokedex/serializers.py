from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Type, Abilities, Category, Pokemon, Statistics


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
    categoryDetail = CategorySerializer(many=True, read_only=True, source='category')
    typeDetail = TypeSerializer(many=True, read_only=True, source='type')
    debilitiesDetail = TypeSerializer(many=True, read_only=True, source='debilities')
    abilitiesDetail = AbilitiesSerializer(read_only=True, source='abilities')

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
            'debilities',
            'categoryDetail',
            'typeDetail',
            'debilitiesDetail',
            'abilitiesDetail'
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
