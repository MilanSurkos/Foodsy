from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.view_basket, name='basket'),
    path('pridat/<int:produkt_id>/', views.add_to_basket, name='add_to_basket'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
]