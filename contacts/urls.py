from django.urls import path

from .api import ContactView, AboutUsView, DeliveriesListView
from .views import contact_detail, about_us_detail


urlpatterns = [
    path('contacts/', contact_detail, name='contacts_detail'),
    path('about-us/', about_us_detail, name='about_us_detail'),
    path('api/contacts/', ContactView.as_view()),
    path('api/about-us/', AboutUsView.as_view()),
    path('api/deliveries/', DeliveriesListView.as_view()),
]