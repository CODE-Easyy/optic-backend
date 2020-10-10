from rest_framework.viewsets import ModelViewSet


from .serializers import CartItemSerializer, CartSerializer
from .models import CartItem, Cart


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
