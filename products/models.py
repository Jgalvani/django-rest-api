from django.db import models

class Categories(models.Model):
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'product_categories'


class Products(models.Model):
    name = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Customers(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=180)
    birthDate = models.DateField()
    password = models.CharField(max_length=45)
    address = models.TextField(max_length=180)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=85)
    country = models.CharField(max_length=85)
    other = models.TextField(max_length=300)


    class Meta:
        db_table = 'product_customers'


class Orders(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(max_length=180)
    address = models.TextField(max_length=180)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=85)
    country = models.CharField(max_length=85)
    other = models.TextField(max_length=300)
    status = models.CharField(max_length=10, default='waiting')
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products, related_name='orders')

    class Meta:
        db_table = 'product_orders'