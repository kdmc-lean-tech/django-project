from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

SEX_CHOISES = [
    ('F', 'FEMALE'),
    ('M', 'MALE')
]


class Type(TimeStampedModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Abilities(TimeStampedModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Pokemon(TimeStampedModel):
    name = models.CharField(max_length=75)
    weight = models.FloatField()
    sex = models.CharField(choices=SEX_CHOISES, max_length=1)
    height = models.FloatField()
    description = models.CharField(max_length=250)
    type = models.ManyToManyField(Type)
    abilities = models.ForeignKey(Abilities, on_delete=models.CASCADE, default=None)
    previousEvolution = models.ForeignKey('self', related_name='previous', null=True, on_delete=models.CASCADE, blank=True)
    laterEvolution = models.ForeignKey('self', related_name='later', null=True, on_delete=models.CASCADE, blank=True)
    category = models.ManyToManyField(Category)
    debilities = models.ManyToManyField(Type, related_name='debilities')

    def __str__(self):
        return self.name


class Statistics(TimeStampedModel):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=None)
    ps = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    specialAttack = models.IntegerField()
    specialDefense = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return str(self.pokemon.name)
