from django.shortcuts import render, get_object_or_404
from .models import Product, Kategorie
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all()
    return render(request, 'products/base.html', {'products': products})

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)  # 10 per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'products/product_list.html', {'products': products})

def kategorie_list(request):
    kategorie = Kategorie.objects.filter(parent__isnull=True)

    return render(request, 'products/kategorie_list.html', {'kategorie': kategorie})

"""def produkty_podla_kategorie(request, kategorie_id):
    kategoria = get_object_or_404(Kategorie, id=kategorie_id)
    produkty = Product.objects.filter(category=kategoria, available=True)
    return render(request, 'products/produkty_podla_kategorie.html', {
        'kategoria': kategoria,
        'produkty': produkty
    })"""

def produkty_podla_kategorie(request, subcategory_id):
    podkategoria = get_object_or_404(Podkategoria, id=subcategory_id)
    produkty = Produkt.objects.filter(podkategoria=podkategoria)
    return render(request, 'products/produkty_podla_kategorie.html', {'produkty': produkty, 'podkategoria': podkategoria})