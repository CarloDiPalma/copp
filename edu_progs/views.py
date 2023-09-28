from django.shortcuts import render

from edu_progs.models import Programm


def index(request):
    progs = Programm.objects.all()

    context = {'progs': progs}
    return render(request, 'edu_progs/index.html', context)
