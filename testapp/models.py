from django.db import models

# Create your models here.
class test_data(models.Model):
    name=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=10)
    address=models.TextField()


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


