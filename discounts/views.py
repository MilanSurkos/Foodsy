from django.shortcuts import render
from products.models import Product

def discount_list(request):
    products = Product.objects.filter(is_discounted=True, discount_price__isnull=False)
    return render(request, 'discounts/discount_list.html', {'products': products})
