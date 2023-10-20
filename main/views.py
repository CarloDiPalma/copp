from django.shortcuts import render

from edu_progs.models import Program
from events.models import Event
from news.models import Post


def index(request):
    progs = Program.objects.filter().order_by('-id')[:3][::-1]
    posts = Post.objects.filter().order_by('-id')[:3][::-1]
    events = Event.objects.filter().order_by('-id')[:3][::-1]

    context = {
        'progs': progs,
        'posts': posts,
        'events': events
    }
    return render(request, 'main/index.html', context)
