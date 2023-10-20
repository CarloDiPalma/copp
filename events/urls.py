from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.event_detail, name='event-detail'),
]
