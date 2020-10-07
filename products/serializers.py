from rest_framework import serializers
from .models import (
    Product,
    OpticalPower,
    Radius,
    Brand,
    Material,
    SubCategory,
    Volume,
)


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'is_discount', 'discount')