from django.urls import path

from . import views

app_name = 'edu_progs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.program_detail, name='program-detail'),
    path('form/<str:pk>/', views.program_form, name='program-form'),
    path('order-success/<str:pk>/', views.program_order_success, name='program-order-success'),
]
