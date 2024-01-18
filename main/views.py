from django.shortcuts import render

from edu_progs.models import Program
from events.models import Event
from news.models import Post
from .models import People


def index(request):
    progs = Program.objects.filter().order_by('-id')[:4][::-1]
    posts = Post.objects.filter().order_by('-id')[:4][::-1]
    events = Event.objects.filter().order_by('-id')[:4][::-1]
    people = People.objects.get(id=1).count
    context = {
        'progs': progs,
        'posts': posts,
        'events': events,
        'people': people
    }
    return render(request, 'main/index.html', context)
