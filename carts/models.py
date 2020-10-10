from django.db import models

from datetime import datetime

from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE),
    count = models.IntegerField()


    def __str__(self):
        return "CartItem(product={}, count={})".format(self.product.id, self.count)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(default=datetime.now)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([i.product.price for i in self.get_cart_items()])

    def __str__(self):
        return "Cart(id={}, sum={})".format(self.id, self.get_cart_total())