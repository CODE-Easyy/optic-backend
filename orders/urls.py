from django.urls import path

from .api import get_order
from .views import  ger_order

urlpatterns = [
    path('api/order/', get_order),
]
