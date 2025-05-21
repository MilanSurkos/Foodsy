from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'templates/products/index.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})