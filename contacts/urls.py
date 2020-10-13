from django.urls import path

from .api import ContactView


urlpatterns = [
    path('api/contacts/', ContactView.as_view()),
]