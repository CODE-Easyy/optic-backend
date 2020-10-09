from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from products.models import Product, SubCategory, Brand, Material


@login_required(login_url='login')
@staff_member_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def products(request):
    products = Product.objects.all()
    subcategories = SubCategory.objects.all()

    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'ВСЕ ПРОДУКТЫ'
    }
    return render(request, 'dashboard/products/products.html', context)

def glasses(request):
    products = Product.objects.filter(cat='glasses')
    subcategories = SubCategory.objects.all()

    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'subcategories': subcategories,
        'title': 'ОЧКИ'
    }
    return render(request, 'dashboard/products/products.html', context)


def glasses_detail(request, pk=None):
    product = Product.objects.get(id=pk)
    subcats = SubCategory.objects.filter(cat=product.cat)
    brands = Brand.objects.all()
    materials = Material.objects.all()
    context = {
        'product': product,
        'subcats': subcats,
        'brands': brands,
        'materials': materials,
    }
    return render(request, 'dashboard/products/detail.html', context)
