from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Event
from .forms import EventForm

def delete_null():
    for event in Event.objects.all():
        if len(event.title) == 0:
            event.delete()

@login_required(login_url='login')
@staff_member_required(login_url='login')
def events(request):
    delete_null()
    events = Event.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search', None)
        events = events.filter(title__icontains=search)

    context = {
        'events': events,
        'title': 'ВСЕ ПРОДУКТЫ'
    }

    return render(request, 'events/events.html', context)

@login_required(login_url='login')
@staff_member_required(login_url='login')
def event_detail(request, pk=None):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    


    if request.method == 'POST':
        # print(request.FILES)
        form = EventForm(request.POST, files=request.FILES, instance=event)
        print(form.errors)
        if form.is_valid():
            print('DATA',form.cleaned_data)
            form.save()
            return redirect('events')

    context = {
        'form':form,
        'event': event,
    }
    return render(request, 'events/detail.html', context)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def event_create(request):
    event = Event()
    event.save()
    return redirect('event_detail', pk=event.pk)


@login_required(login_url='login')
@staff_member_required(login_url='login')
def event_delete(request, pk=None):
    event = Event.objects.get(pk=pk)
    event.delete()
    return redirect('events')
