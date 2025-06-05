from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_basket(request):
    basket = request.session.get('basket', {})
    # Ochrana: ak nie je dict, inicializuj znova
    if not isinstance(basket, dict):
        basket = {}
        request.session['basket'] = basket

    basket_items = []
    total_price = 0

    for produkt_id_str, quantity in basket.items():
        produkt = get_object_or_404(Product, id=int(produkt_id_str))
        item_total = produkt.price * quantity
        basket_items.append({
            'product': produkt,
            'quantity': quantity,
            'total_price': round(item_total, 2)
        })
        total_price += item_total

    return render(request, 'basket/view_basket.html', {
        'basket_items': basket_items,
        'total_price': round(total_price, 2)
    })


def add_to_basket(request, produkt_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        produkt_id_str = str(produkt_id)

        basket = request.session.get('basket', {})

        # Ochrana: ak nie je dict, inicializuj znova
        if not isinstance(basket, dict):
            basket = {}

        if produkt_id_str in basket:
            basket[produkt_id_str] += quantity
        else:
            basket[produkt_id_str] = quantity

        request.session['basket'] = basket
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')