from django.db import models
from django.conf import settings

class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='potomci'
    )
    # Ak je rodic = None, je to hlavná kategória (napr. Jedlo, Pitie, Ostatné)
    # Ak má rodiča, tak je to podkategória alebo pod-podkategória

    def __str__(self):
        return self.nazev


class Product(models.Model):
    PRODUCT_TYPES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='product/images/', blank=True, null=True)

    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE, related_name='produkty')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
