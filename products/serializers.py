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



class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'is_discount', 'discount', 'img_1', 'is_new', 'is_leader')

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'is_discount', 'discount', 'material', 'brand', 'img_1', 'img_2', 'img_3', 'sex')