from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    whats_app_phone = models.CharField(max_length=100, null=True, blank=True)


    vk_url = models.URLField(max_length=255, null=True, blank=True)
    insta_url = models.URLField(max_length=255, null=True, blank=True)
