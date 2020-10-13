from django.urls import path

from .api import ContactView, AboutUsView


urlpatterns = [
    path('api/contacts/', ContactView.as_view()),
    path('api/about-us/', AboutUsView.as_view()),
]