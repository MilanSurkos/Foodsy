from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
]
