from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('next/', views.next, name='next'),
    ]

