from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Order, OrderItem
from products.models import Product

def add_order_item(item: dict) -> dict:
    product = Product.objects.get(id=item['id'])
    order_item = OrderItem.objects.get_or_create(
        product=product,
        count=item['count'])
    res = order_item[0]
    return res


@api_view(['POST'])
def get_order(request):
    if request.method == 'POST':
        data = request.data

        if 'products' in data:
            products = data['products']
            products = list(map(add_order_item, products))
            order = Order(
                name=data['name'],
                address=data['adress'],
                comment=data['comment'],
                phone=data['phone'],
                email=data['email']
            )
            order.save()
            for pr in products:
                order.products.add(pr)



        return Response({'asd':'asd'},status=status.HTTP_200_OK)