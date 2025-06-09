from products.models import Kategorie

def kategorie_processor(request):
    return {
        'vsetky_kategorie': Kategorie.objects.filter(parent__isnull=True)
    }
