from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from products.models import Product

@login_required
def orders_view(request):
    """
    Display all orders for the logged-in user, including order items and delivery cost.
    """
    orders = Order.objects.filter(user=request.user)\
        .order_by('-date')\
        .prefetch_related('items__product')

    for order in orders:
        # Calculate total price for each order
        total = 0
        for item in order.items.all():
            item.total_price = item.quantity * item.price
            total += item.total_price
        order.total_price = total

        # Calculate delivery cost based on total price
        order.delivery_cost = 0 if order.total_price > 1000 else 300

    return render(request, 'orders/orders_list.html', {'orders': orders})


@login_required
def create_order(request):
    """
    Create a new order from items stored in session basket.
    """
    basket = request.session.get('basket', {})

    if not basket:
        messages.warning(request, "Košík je prázdny.")
        return redirect('basket:view_basket')

    if request.method == 'POST':
        address = request.POST.get('delivery_address', '').strip()

        if not address:
            messages.error(request, "Zadajte doručovaciu adresu.")
            return redirect('orders:create_order')

        # Optional: Add validation for delivery_date, delivery_time here if needed

        # Create the Order object
        order = Order.objects.create(
            user=request.user,
            delivery_address=address,
            # Add other fields here if you extend your model
        )

        # Create OrderItem entries for each product in the basket
        for product_id, quantity in basket.items():
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                messages.error(request, f"Produkt s ID {product_id} neexistuje.")
                continue  # skip this item

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

        # Clear the basket after order is placed
        request.session['basket'] = {}

        messages.success(request, "Objednávka bola úspešne vytvorená.")
        return redirect('orders:orders')

    # If GET request, just render the form template
    delivery_time_choices = Order.DELIVERY_TIME_CHOICES
    return render(request, 'orders/create_order.html', {'delivery_time_choices': delivery_time_choices})
