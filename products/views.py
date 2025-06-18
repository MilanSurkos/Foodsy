from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Kategorie, Product

try:
    from django.db.models.functions import Unaccent
    HAS_UNACCENT = True
except ImportError:
    HAS_UNACCENT = False


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


def product_search(request):
    import unicodedata
    def normalize(text):
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii').lower()

    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        norm_query = normalize(query)
        if HAS_UNACCENT:
            products = products.annotate(
                cat_name=Lower(Unaccent('category__nazev')),
                parent_name=Lower(Unaccent('category__parent__nazev')),
                parent2_name=Lower(Unaccent('category__parent__parent__nazev')),
                prod_name=Lower(Unaccent('name')),
            ).filter(
                Q(prod_name__contains=norm_query) |
                Q(cat_name__contains=norm_query) |
                Q(parent_name__contains=norm_query) |
                Q(parent2_name__contains=norm_query)
            ).distinct()
        else:
            # Fallback: remove accents from query and compare lowercased
            products = [p for p in products if norm_query in normalize(p.name) or
                        norm_query in normalize(p.category.nazev) or
                        (p.category.parent and norm_query in normalize(p.category.parent.nazev)) or
                        (p.category.parent and p.category.parent.parent and norm_query in normalize(p.category.parent.parent.nazev))]
    return render(request, 'products/product_search_results.html', {'products': products, 'query': query})