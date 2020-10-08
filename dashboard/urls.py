from django.urls import path

from .views import  (
    dashboard,
    products,
    glasses,
    glasses_detail
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('products/glasses/', glasses, name='glasses'),
    path('products/glasses/detail/<int:pk>/', glasses_detail, name='glasses_detail'),
]