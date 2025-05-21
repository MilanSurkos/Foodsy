from django.shortcuts import render

# Create your views here.
# basket/views.py
from django.shortcuts import render

def view_basket(request):
    return render(request, 'basket/view_basket.html')
