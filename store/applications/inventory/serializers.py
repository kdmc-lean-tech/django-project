from rest_framework import serializers
from .models import Vendor, Product


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'name',
            'description'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'code',
            'description',
            'price',
            'stock',
            'iva',
            'weigth',
            'vendor'
        )


