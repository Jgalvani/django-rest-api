# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    name = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.IntegerField()
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'products'