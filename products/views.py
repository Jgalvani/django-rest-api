from rest_framework import generics, authtoken, permissions

from .models import Products
from .serializers import ProductSerializer


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
    queryset = Products.objects.values()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]