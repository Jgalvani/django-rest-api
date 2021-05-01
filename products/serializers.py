from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products

        fields = [
            'pk',
            'name',
            'description',
            'price',
            'stock',
            'category',
            'image',
            'created_at',
        ]

        meta_kwargs = {
            'created_at': { 'required': False },
            'image': { 'required': False },
            'description': { 'required': False },
            'category': { 'required': False },
        }

