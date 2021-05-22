from rest_framework import generics, authtoken, permissions

from .models import  Categories, Products, Customers, Orders
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer


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



class customerList(generics.ListCreateAPIView):
    """
    Get all customers
    """
    queryset = Customers.objects.values()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class customerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Edit a customer
    """
    queryset = Customers.objects
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class orderList(generics.ListCreateAPIView):
    """
    Get all orders
    """
    queryset = Orders.objects.values()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class orderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Edit a order
    """
    queryset = Orders.objects
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
