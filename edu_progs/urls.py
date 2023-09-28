from django.urls import path

from . import views

app_name = 'edu_progs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.program_detail, name='program-detail'),
]
