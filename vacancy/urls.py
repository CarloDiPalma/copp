from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.vacancy_detail, name='vacancy-detail'),
]
