from django.urls import path

from .views import ger_order

urlpatterns = [
    path('order/', ger_order),
]