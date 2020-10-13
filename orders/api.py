from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Order, OrderItem
from products.models import Product

def add_order_item(item: dict) -> dict:
    res = dict()
    product = Product.objects.get(id=item['id'])
    order_item = OrderItem.objects.get_or_create(
        product=product,
        count=item['count'])
    res['id'] = order_item[0].id
    return res


@api_view(['POST'])
def get_order(request, format=None):
    if request.method == 'POST':
        data = request.data
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
        map(order.products.add, products)




        return Response({'asd':'asd'},status=status.HTTP_200_OK)