from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib import messages

from products.forms import GlassesForm, FramesForm
from products.models import Product, SubCategory, Brand, Material


@login_required(login_url='login')
@staff_member_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='login')
@staff_member_required(login_url='login')
def products(request):
    products = Product.objects.all()
    subcategories = SubCategory.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        products = products.filter(title__contains=search)

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'ВСЕ ПРОДУКТЫ'
    }
    return render(request, 'dashboard/products/products.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def glasses(request):
    products = Product.objects.filter(cat='glasses')
    subcategories = SubCategory.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        products = products.filter(title__contains=search)


    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'ОЧКИ'
    }
    return render(request, 'dashboard/products/products.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def outlets(request):
    products = Product.objects.filter(cat='outlet')
    subcategories = SubCategory.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        products = products.filter(title__contains=search)


    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'OUTLETS'
    }
    return render(request, 'dashboard/products/products.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def frames(request):
    products = Product.objects.filter(cat='frames')
    subcategories = SubCategory.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        products = products.filter(title__contains=search)


    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'Линзы'
    }
    return render(request, 'dashboard/products/products.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_glasses(request):
    form = GlassesForm()

    if request.method == 'POST':
        form = GlassesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/products/create.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_frame(request):
    form = FramesForm()

    if request.method == 'POST':
        form = FramesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/products/create.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def glasses_detail(request, pk=None):
    product = Product.objects.get(id=pk)
    form = GlassesForm(instance=product, cat=product.cat)
    if request.method == 'POST':
        print(request.POST)
        form = GlassesForm(request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form':form,
        'product': product,
    }
    return render(request, 'dashboard/products/detail.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def frames_detail(request, pk=None):
    product = Product.objects.get(id=pk)
    form = FramesForm(instance=product, cat=product.cat)
    if request.method == 'POST':
        print(request.POST)
        form = GlassesForm(request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form':form,
        'product': product,
    }

    return render(request, 'dashboard/products/detail.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_glasses(request, pk=None):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('products')
    context = {
        'item': item.title
    }
    return render(request, 'dashboard/products/delete.html', context)

