from django.urls import path, include
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]
