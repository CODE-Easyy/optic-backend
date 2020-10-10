from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from products.models import (
    Brand,
    Material,
    Radius,
    OpticalPower,
    Volume
)
from .forms import (
    BrandForm,
    MaterialForm,
    RadiusForm,
    OpticalPowerForm,
    VolumeForm,
)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def filters(request):
    brands = Brand.objects.all()
    materials = Material.objects.all()
    radiuses = Radius.objects.all()
    optical_powers = OpticalPower.objects.all()
    volumes = Volume.objects.all()
    context = {
        'brands': brands,
        'materials': materials,
        'radiuses': radiuses,
        'optical_powers': optical_powers,
        'volumes': volumes,
    }
    return render(request, 'filters/filters.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_brand(request):
    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filters')

    context = {
        'form': form,
    }
    return render(request, 'filters/create.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_material(request):
    form = MaterialForm()

    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filters')

    context = {
        'form': form,
    }
    return render(request, 'filters/create.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_radius(request):
    form = RadiusForm()

    if request.method == 'POST':
        form = RadiusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filters')

    context = {
        'form': form,
    }
    return render(request, 'filters/create.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_opt_power(request):
    form = OpticalPowerForm()

    if request.method == 'POST':
        form = OpticalPowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filters')

    context = {
        'form': form,
    }
    return render(request, 'filters/create.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def create_volume(request):
    form = VolumeForm()

    if request.method == 'POST':
        form = VolumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filters')

    context = {
        'form': form,
    }
    return render(request, 'filters/create.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_brand(request, pk=None):
    item = Brand.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('filters')
    context = {
        'item': item.value
    }
    return render(request, 'filters/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_material(request, pk=None):
    item = Material.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('filters')
    context = {
        'item': item.value
    }
    return render(request, 'filters/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_radius(request, pk=None):
    item = Radius.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('filters')
    context = {
        'item': item.value
    }
    return render(request, 'filters/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_opt_power(request, pk=None):
    item = OpticalPower.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('filters')
    context = {
        'item': item.value
    }
    return render(request, 'filters/delete.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete_volume(request, pk=None):
    item = Volume.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('filters')
    context = {
        'item': item.value
    }
    return render(request, 'filters/delete.html', context)