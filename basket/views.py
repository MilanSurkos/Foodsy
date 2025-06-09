from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from products.models import Product


def view_basket(request):
    basket = request.session.get('basket', {})

    # Ak basket nie je dict, inicializuj ho znovu
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


@require_POST
def add_to_basket(request, produkt_id):
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1

    produkt_id_str = str(produkt_id)
    basket = request.session.get('basket', {})

    if not isinstance(basket, dict):
        basket = {}

    # Pridanie alebo zvýšenie množstva produktu v košíku
    basket[produkt_id_str] = basket.get(produkt_id_str, 0) + quantity
    request.session['basket'] = basket

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'quantity': basket[produkt_id_str]
        })

    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_POST
def update_quantity(request):
    produkt_id = request.POST.get('produkt_id')
    action = request.POST.get('action')

    basket = request.session.get('basket', {})

    if not isinstance(basket, dict):
        basket = {}

    if produkt_id in basket:
        if action == 'inc':
            basket[produkt_id] += 1
        elif action == 'dec' and basket[produkt_id] > 1:
            basket[produkt_id] -= 1
        else:
            # Ak je množstvo 1 a pokus o decrement, nechaj tak
            pass

        request.session['basket'] = basket
        return JsonResponse({'success': True, 'new_qty': basket[produkt_id]})

    return JsonResponse({'success': False})


@require_POST
def remove_from_basket(request):
    produkt_id = request.POST.get('produkt_id')

    if not produkt_id:
        return HttpResponseBadRequest("Chýba produkt_id.")

    basket = request.session.get('basket', {})

    if not isinstance(basket, dict):
        basket = {}

    if produkt_id in basket:
        del basket[produkt_id]
        request.session['basket'] = basket
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})