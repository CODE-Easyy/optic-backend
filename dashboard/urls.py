from django.urls import path

from .views import (
    dashboard,
    products,
    glasses,
    glasses_detail,
    create_glasses,
    delete_glasses,
    frames_detail,
    create_frame,
    frames,
    outlets,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('products/glasses/', glasses, name='glasses'),
    path('products/glasses/detail/<int:pk>/', glasses_detail, name='glasses_detail'),
    path('products/glasses/create/', create_glasses, name='glasses_create'),
    path('products/delete/<int:pk>/', delete_glasses, name='glasses_delete'),

    path('products/frames/', frames, name='frames'),
    path('products/frames/detail/<int:pk>/', frames_detail, name='frame_detail'),
    path('products/frames/create/', create_frame, name='frame_create'),

    path('products/outlets/', outlets, name='outlets'),

]
