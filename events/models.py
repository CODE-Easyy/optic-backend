from django.db import models
from datetime import datetime

from products.models import Product




class Event(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='events', null=True, blank=True)
    img_slide = models.ImageField(upload_to='events', null=True, blank=True)
    from_date = models.DateTimeField(default=datetime.now)
    to_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    products = models.ManyToManyField(Product)