from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .serializers import DetailEventSerializer, SlideEventSerializer
from .models import Event


class SlideEventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = SlideEventSerializer

class DetailEventView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = DetailEventSerializer



