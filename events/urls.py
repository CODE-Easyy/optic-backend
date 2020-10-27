from django.urls import path



from .api import (
    DetailEventView,
    SlideEventList
)


from .views import (
    events,
    event_detail,
    event_create,
    event_delete
)

urlpatterns = [
    path('list/', SlideEventList.as_view()),
    path('detail/<int:pk>/', DetailEventView.as_view()),



    path('dashboard/events/', events, name='events'),
    path('dashboard/create/event/', event_create, name='event_create'),
    path('dashboard/event/detail/<pk>', event_detail, name='event_detail'),
    path('dashboard/event/delete/<pk>', event_delete, name='event_delete'),
]