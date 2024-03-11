from django.shortcuts import render

from .models import Vacancy


def index(request):
    vacancies = Vacancy.objects.all()

    context = {'vacancies': vacancies}
    return render(request, 'vacancy/index.html', context)


def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    context = {'vacancy': vacancy}
    return render(request, 'vacancy/vacancy_detail.html', context)
