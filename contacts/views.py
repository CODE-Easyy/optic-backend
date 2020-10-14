from django.shortcuts import render

from .models import Contact, AboutUs
from .forms import ContactForm, AboutUsForm


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