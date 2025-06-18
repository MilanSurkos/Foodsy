from django.shortcuts import render, get_object_or_404, redirect
from products.models import Kategorie, Product


def kategorie_list(request):
    context = {
        "kategorie_list": Kategorie.objects.all()
    }
    return render(request, 'products/category_list.html', context)


def produkty_podla_kategorie(request, category_id):
    kategoria = get_object_or_404(Kategorie, id=category_id)
    products = kategoria.produkty.all()

    if request.method == 'POST':
        produkt_id = request.POST.get('produkt_id')
        if produkt_id:
            basket = request.session.get('basket', {})
            basket[produkt_id] = basket.get(produkt_id, 0) + 1
            request.session['basket'] = basket
            return redirect('products:produkty_podla_kategorie', category_id=category_id)

    return render(request, 'products/product_list.html', {
        'products': products,
        'kategoria': kategoria,
        'basket': request.session.get('basket', {}),
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    category = product.category
    return render(request, 'products/product_detail.html', {
        'product': product,
        'category': category,
    })


def slevy_list(request):
    produkty = Product.objects.filter(is_discounted=True, discount_price__isnull=False)
    return render(request, 'products/product_list.html', {'products': produkty})