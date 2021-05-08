from rest_framework import generics, authtoken, permissions

from .models import Products, Categories
from .serializers import ProductSerializer, CategorySerializer


class productList(generics.ListCreateAPIView):
    """
    Get all products
    """
    queryset = Products.objects.values()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class productDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Edit a product
    """
    queryset = Products.objects
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class categoryList(generics.ListCreateAPIView):
    """
    Get all categories
    """
    queryset = Categories.objects.values()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Edit a category
    """
    queryset = Categories.objects
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
