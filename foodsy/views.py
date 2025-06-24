# foodsy/views.py
from django.shortcuts import render
from products.models import Product

def home(request):
    featured_products = Product.objects.all()[:4]  # Just show first 4
    discounts_products = Product.objects.filter(is_discounted=True, discount_price__isnull=False)
    basket = request.session.get('basket', {})
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'discounts_products': discounts_products,
        'basket': basket,
    })