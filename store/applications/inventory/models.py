from django.db import models
from django.db.models import FloatField
from model_utils.models import TimeStampedModel
# Create your models here.


class Vendor(TimeStampedModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=75)
    code = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    iva = models.IntegerField()
    weigth: FloatField = models.FloatField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create model Any