from rest_framework import serializers

from .models import Categories, Products, Customers, Orders


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories

        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products

        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'image',
            'created_at',
            'category_id',
        ]

        meta_kwargs = {
            'created_at': { 'required': False },
            'image': { 'required': False },
        }




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders

        fields = [
            'id',
            'firstName',
            'lastName',
            'email',
            'address',
            'zipcode',
            'city',
            'country',
            'other',
            'status',
            'customer_id',
        ]
