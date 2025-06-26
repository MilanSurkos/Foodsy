from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView

app_name = 'products'

urlpatterns = [
    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('kategoria/<int:category_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
    path('produkt/<int:product_id>/', views.product_detail, name='product_detail'),  # detail produktu
    path('search/', views.product_search, name='product_search'),
    path('', ProductListView.as_view(), name='product-list'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
]
