from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class Character(TimeStampedModel):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Power(TimeStampedModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    character = models.ManyToManyField(Character)

    def __str__(self):
        return self.name
