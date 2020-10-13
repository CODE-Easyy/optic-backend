from django.urls import path

from .api import ContactView, AboutUsView, DeliveriesListView


urlpatterns = [
    path('api/contacts/', ContactView.as_view()),
    path('api/about-us/', AboutUsView.as_view()),
    path('api/deliveries/', DeliveriesListView.as_view()),
]