from django.db import models

from products.models import Product

from datetime import datetime

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    count = models.IntegerField()

    def __str__(self):
        return f"OrderItem({self.pk} ,{self.product.title}, {self.count})"

class Order(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    products = models.ManyToManyField(OrderItem)
    date = models.DateTimeField(default=datetime.now)