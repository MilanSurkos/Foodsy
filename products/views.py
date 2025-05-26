from django.shortcuts import render

from products.models import Kategorie


def kategorie_list(request):
    """jedlo_sub = [
        {
            'name': 'Čerstvé potraviny',
            'subsubcategories': [
                {'id': 10, 'name': 'Ovocie'},
                {'id': 11, 'name': 'Zelenina'},
                {'id': 12, 'name': 'Mliečne výrobky'},
            ]
        },
        {
            'name': 'Trvanlivé potraviny',
            'subsubcategories': [
                {'id': 13, 'name': 'Konzervy'},
                {'id': 14, 'name': 'Sušené potraviny'},
                {'id': 15, 'name': 'Cestoviny a ryža'},
            ]
        },
        {
            'name': 'Mrazené potraviny',
            'subsubcategories': [
                {'id': 16, 'name': 'Mrazená zelenina'},
                {'id': 17, 'name': 'Mrazené ovocie'},
                {'id': 18, 'name': 'Mrazené mäsové výrobky'},
            ]
        }
    ]

    pitie_sub = [
        {
            'name': 'Nealkoholické nápoje',
            'subsubcategories': [{'id': 4, 'name': 'Nealkoholické nápoje'}]
        },
        {
            'name': 'Alkoholické nápoje',
            'subsubcategories': [{'id': 5, 'name': 'Alkoholické nápoje'}]
        },
        {
            'name': 'Teplé nápoje',
            'subsubcategories': [{'id': 6, 'name': 'Teplé nápoje'}]
        },
    ]

    ostatne_sub = [
        {
            'name': 'Domácnosť a hygiena',
            'subsubcategories': [{'id': 7, 'name': 'Domácnosť a hygiena'}]
        },
        {
            'name': 'Pre deti a domácich miláčikov',
            'subsubcategories': [{'id': 8, 'name': 'Pre deti a domácich miláčikov'}]
        },
        {
            'name': 'Drobný tovar a sezónne veci',
            'subsubcategories': [{'id': 9, 'name': 'Drobný tovar a sezónne veci'}]
        },
    ]

    context = {
        'jedlo_sub': jedlo_sub,
        'pitie_sub': pitie_sub,
        'ostatne_sub': ostatne_sub,
    } """
    context = {"kategorie_list": Kategorie.objects.all()}

    return render(request, 'products/kategorie_list.html', context)


def produkty_podla_kategorie(request, category_id):
    kategorie = Kategorie.objects.get(id=category_id)
    return render(request, 'products/produkty_podla_kategorie.html', {'category_id': category_id,
                                                                      'produkty': kategorie.produkty.all })