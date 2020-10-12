from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def get_order(request, format=None):
    if request.method == 'POST':
        print(request.data)


        return Response({'asd':'asd'},status=status.HTTP_200_OK)