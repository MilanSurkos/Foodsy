from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('kategoria/<int:category_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
    path('produkt/<int:product_id>/', views.product_detail, name='product_detail'),  # detail produktu
]