from django.shortcuts import render

from edu_progs.models import Program


def index(request):
    progs = Program.objects.all()

    context = {'progs': progs}
    return render(request, 'edu_progs/index.html', context)


def program_detail(request, pk):
    program = Program.objects.get(id=pk)
    context = {'program': program}
    return render(request, 'edu_progs/program_detail.html', context)
