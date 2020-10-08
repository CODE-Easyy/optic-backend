from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from products.models import Product, SubCategory
from products.forms import GlassesDetailForm


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


class GlassesDetailView(UpdateView):
    model = Product
    template_name = 'dashboard/products/detail.html'
    form_class = GlassesDetailForm
    success_url = reverse_lazy('products')
