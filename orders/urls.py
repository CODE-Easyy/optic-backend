from django.urls import path

from .api import get_order
from .views import orders_list, order_detail,delete_order

urlpatterns = [
    path('api/order/', get_order),
    path('orders/', orders_list, name='orders'),
    path('orders/detail/<int:pk>/', order_detail, name='order_detail'),
    path('orders/delete/<int:pk>/', delete_order, name='order_delete')
]
