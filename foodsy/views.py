# foodsy/views.py
from django.shortcuts import render
from products.models import Product

def home(request):
    featured_products = Product.objects.all()[:4]  # Just show first 4
    return render(request, 'home.html', {'featured_products': featured_products})