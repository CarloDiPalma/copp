from django.shortcuts import render, redirect
from django.urls import reverse

from edu_progs.forms import OrderForm
from edu_progs.models import Order, Program


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
        print(order.pk)
        return redirect(reverse('edu_progs:program-order-success', kwargs={'pk': order.pk}))
    context = {'program': program, 'form': form}
    return render(request, 'edu_progs/program_form.html', context)


def program_order_success(request, pk):
    order = Order.objects.get(id=pk)

    context = {'order': order}
    return render(request, 'edu_progs/program_order_success.html', context)
