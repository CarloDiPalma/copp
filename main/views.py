from django.shortcuts import render

from edu_progs.models import Program
from events.models import Event
from news.models import Post
from vacancy.models import Vacancy
from .models import People

POSTS_NUMBER = 4


def index(request):
    progs = Program.objects.filter().order_by('-id')[:POSTS_NUMBER][::-1]
    posts = Post.objects.filter().order_by('-id')[:POSTS_NUMBER][::-1]
    events = Event.objects.filter().order_by('-id')[:POSTS_NUMBER][::-1]
    vacancies = Vacancy.objects.filter().order_by('-id')[:POSTS_NUMBER][::-1]
    try:
        people = People.objects.get(id=1).count
    except:
        people = 76398
    context = {
        'progs': progs,
        'posts': posts,
        'events': events,
        'people': people,
        'vacancies': vacancies
    }
    return render(request, 'main/index.html', context)
