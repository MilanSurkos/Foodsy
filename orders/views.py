from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from products.models import Product

@login_required
def orders_view(request):
    # Fetch user's orders with related items and products for efficiency
    orders = Order.objects.filter(user=request.user).order_by('-date').prefetch_related('items__product')

    for order in orders:
        total = 0
        for item in order.items.all():
            item.total_price = item.quantity * item.price  # Total price per item
            total += item.total_price
        order.total_price = total  # Total price for the order

        # Delivery cost logic
        if order.total_price > 1000:
            order.delivery_cost = 0
        else:
            order.delivery_cost = 300

    return render(request, 'orders/orders_list.html', {'orders': orders})

@login_required
def create_order(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.warning(request, "Košík je prázdny.")
        return redirect('basket:view_basket')

    if request.method == 'POST':
        address = request.POST.get('delivery_address')
        if not address:
            messages.error(request, "Zadajte doručovaciu adresu.")
            return redirect('orders:create_order')

        order = Order.objects.create(user=request.user, delivery_address=address)

        for product_id, quantity in basket.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

        request.session['basket'] = {}
        messages.success(request, "Objednávka bola úspešne vytvorená.")
        return redirect('orders:orders')

    return render(request, 'orders/create_order.html')
