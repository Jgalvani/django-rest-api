from rest_framework import serializers

from .models import Products, Categories


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products

        fields = '__all__'

        meta_kwargs = {
            'created_at': { 'required': False },
            'image': { 'required': False },
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories

        fields = '__all__'
