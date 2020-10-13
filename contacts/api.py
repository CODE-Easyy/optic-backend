from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK



from .serializers import ContactSerializer
from .models import Contact



class ContactView(RetrieveAPIView):
    queryset = Contact.objects.all()

    def get(self, request, *args, **kwargs):
        Contact.objects.get_or_create(id=1)
        q = Contact.objects.all().first()
        serializer = ContactSerializer(q)
        return Response(serializer.data, status=HTTP_200_OK)
