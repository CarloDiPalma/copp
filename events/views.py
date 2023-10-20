from django.shortcuts import render

from .models import Event


def index(request):
    events = Event.objects.all()

    context = {'events': events}
    return render(request, 'events/index.html', context)


def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)
