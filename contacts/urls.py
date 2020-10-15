from django.urls import path

from .api import ContactView, AboutUsView, DeliveriesListView
from .views import contact_detail, about_us_detail, deliveries, create_delivery, delivery_detail, delete_delivery


urlpatterns = [
    path('dashboard/contacts/', contact_detail, name='contacts_detail'),
    path('dashboard/about-us/', about_us_detail, name='about_us_detail'),
    path('dashboard/deliveries/', deliveries, name='deliveries'),
    path('dashboard/delivery/create/', create_delivery, name='delivery_create'),
    path('dashboard/delivery/detail/<int:pk>', delivery_detail, name='delivery_detail'),
    path('dashboard/delivery/delete/<int:pk>', delete_delivery, name='delivery_delete'),
    path('api/contacts/', ContactView.as_view()),
    path('api/about-us/', AboutUsView.as_view()),
    path('api/deliveries/', DeliveriesListView.as_view()),
]