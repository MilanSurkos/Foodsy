from django.shortcuts import render, get_object_or_404, redirect
from products.models import Kategorie, Product


def kategorie_list(request):
    context = {
        "kategorie_list": Kategorie.objects.all()
    }
    return render(request, 'products/kategorie_list.html', context)


def produkty_podla_kategorie(request, category_id):
    kategoria = get_object_or_404(Kategorie, id=category_id)
    produkty = kategoria.produkty.all()

    if request.method == 'POST':
        produkt_id = request.POST.get('produkt_id')
        if produkt_id:
            basket = request.session.get('basket', {})
            basket[produkt_id] = basket.get(produkt_id, 0) + 1
            request.session['basket'] = basket
            return redirect('products:produkty_podla_kategorie', category_id=category_id)

    return render(request, 'products/produkty_podla_kategorie.html', {
        'produkty': produkty,
        'kategoria': kategoria,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})