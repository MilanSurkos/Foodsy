from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def orders_view(request):
    return render(request, 'orders/orders.html')
