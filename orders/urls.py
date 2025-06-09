from django.urls import path
from . import views

app_name = 'orders'  # pridaný namespace

urlpatterns = [
    path('', views.orders_view, name='orders'),
    path('create/', views.create_order, name='create_order'),  # táto cesta musí existovať
]
