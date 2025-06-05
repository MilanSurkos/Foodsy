from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def view_basket(request):
    basket = request.session.get('basket', {})
    products = Product.objects.filter(id__in=basket.keys())
    basket_items = []

    total_price = 0
    for product in products:
        quantity = basket.get(str(product.id), 0)
        item_total = product.price * quantity
        total_price += item_total
        basket_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': item_total
        })

    context = {
        'basket_items': basket_items,
        'total_price': total_price,
    }
    return render(request, 'basket/view_basket.html', context)



def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket = request.session.get('basket', {})

    if str(product_id) in basket:
        basket[str(product_id)] += 1
    else:
        basket[str(product_id)] = 1

    request.session['basket'] = basket
    return redirect('basket:view_basket')
