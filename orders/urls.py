from django.urls import path

from .api import get_order

urlpatterns = [
    path('order/', get_order),
]