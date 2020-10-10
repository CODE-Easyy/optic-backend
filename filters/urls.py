from django.urls import path

from .views import  (
    filters,
    create_brand,
    create_material,
    create_radius,
    create_opt_power,
    create_volume,
    delete_brand,
    delete_material,
    delete_opt_power,
    delete_radius,
    delete_volume,
)

urlpatterns = [
    path('filters/lists/', filters, name='filters'),

    path('filters/brands/create/', create_brand, name='brand_create'),
    path('filters/materials/create/', create_material, name='material_create'),
    path('filters/radiuses/create/', create_radius, name='radius_create'),
    path('filters/optical-powers/create/', create_opt_power, name='opt_power_create'),
    path('filters/volumes/create/', create_volume, name='volume_create'),

    path('filters/brands/delete/<int:pk>/', delete_brand, name='brand_delete'),
    path('filters/materials/delete/<int:pk>/', delete_material, name='material_delete'),
    path('filters/radiuses/delete/<int:pk>/', delete_radius, name='radius_delete'),
    path('filters/optical-powers/delete/<int:pk>/', delete_opt_power, name='opt_power_delete'),
    path('filters/volumes/delete/<int:pk>/', delete_volume, name='volume_delete'),

]