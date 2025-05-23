from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('kategorie/<int:kategorie_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
    path('kategoria/<int:subcategory_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
]
