from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .models import Order, OrderItem
from .forms import OrderForm

@login_required(login_url='login')
@staff_member_required(login_url='login')
def order_detail(request, pk=None):
    order = Order.objects.get(id=pk)
    order.is_seen = True
    order.save()
    products = order.get_products()
    form = OrderForm(instance=order)
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {
        'form':form,
        'order': order,
        'products': products,
    }
    return render(request, 'orders/detail.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_order(request, pk=None):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('orders')
    context = {
        'item': f'Заказ ID: {item.id}'
    }
    return render(request, 'orders/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def orders_list(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        orders = orders.filter(id=int(search))

    context = {
        'orders': orders,
        'title': 'ЗАКАЗЫ'
    }
    return render(request, 'orders/orders.html', context)