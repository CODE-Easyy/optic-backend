from django.urls import path



from .api import (
    DetailEventView,
    SlideEventList
)

urlpatterns = [
    path('list/', SlideEventList.as_view()),
    path('detail/<int:pk>/', DetailEventView.as_view()),
]