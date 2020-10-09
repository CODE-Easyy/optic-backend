from django.urls import path

from .views import (
    dashboard,
    products,
    glasses,
    glasses_detail,
    create_glasses,
    delete_glasses,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('products/glasses/', glasses, name='glasses'),
    path('products/glasses/detail/<int:pk>/', glasses_detail, name='glasses_detail'),
    path('products/glasses/create/', create_glasses, name='glasses_create'),
    path('products/glasses/delete/<int:pk>/', delete_glasses, name='glasses_delete'),

    path('products/frames/detail/<int:pk>/', glasses_detail, name='frame_detail'),

]
