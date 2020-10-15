from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Contact, AboutUs, Delivery
from .forms import ContactForm, AboutUsForm, DeliveryForm


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_delivery(request):
    form = DeliveryForm()


    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deliveries')

    context = {
        'form': form,
    }
    return render(request, 'delivery/create.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def deliveries(request):
    deliveries = Delivery.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        deliveries = deliveries.filter(title__contains=search)



    context = {
        'deliveries': deliveries,
        'title': 'Доставки'
    }
    return render(request, 'delivery/deliveries.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def delivery_detail(request, pk=None):
    subcat = Delivery.objects.get(id=pk)
    form = DeliveryForm(instance=subcat)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=subcat)
        if form.is_valid():
            form.save()
            return redirect('deliveries')
    context = {
        'form':form,
        'delivery': subcat,
    }

    return render(request, 'delivery/detail.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_delivery(request, pk=None):
    item = Delivery.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('deliveries')
    context = {
        'item': item.title
    }
    return render(request, 'delivery/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def about_us_detail(request):
    c = AboutUs.objects.all().first()
    form = AboutUsForm(instance=c)

    if request.method == 'POST':
        form = AboutUsForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'title': 'О нас'

            }
            return render(request, 'contacts/detail.html', context)

    context = {
        'form': form,
        'title': 'О нас'
    }
    return render(request, 'contacts/detail.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def contact_detail(request):
    c = Contact.objects.all().first()
    form = ContactForm(instance=c)


    if request.method == 'POST':
        form = ContactForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'title': 'Контакты'

            }
            return render(request, 'contacts/detail.html', context)

    context = {
        'form': form,
        'title': 'Контакты'

    }
    return render(request, 'contacts/detail.html', context)