from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def view_basket(request):
    basket = request.session.get('basket', [])
    produkty = Product.objects.filter(id__in=basket)
    return render(request, 'basket/view_basket.html', {'produkty': produkty})

def add_to_basket(request, produkt_id):
    if request.method == 'POST':
        basket = request.session.get('basket', [])
        if produkt_id not in basket:
            basket.append(produkt_id)
            request.session['basket'] = basket
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')