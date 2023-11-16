from django.shortcuts import render, redirect

from edu_progs.forms import OrderForm
from edu_progs.models import Program


def index(request):
    progs = Program.objects.all()

    context = {'progs': progs}
    return render(request, 'edu_progs/index.html', context)


def program_detail(request, pk):
    program = Program.objects.get(id=pk)
    context = {'program': program}
    return render(request, 'edu_progs/program_detail.html', context)


def program_form(request, pk):
    program = Program.objects.get(id=pk)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.program = program
        order.save()
        return redirect('edu_progs:index')
    context = {'program': program, 'form': form}
    return render(request, 'edu_progs/program_form.html', context)
