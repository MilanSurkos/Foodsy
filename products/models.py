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

    UNIT_CHOICES = [
        ('ks', 'ks'),
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('l', 'l'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='product/images/', blank=True, null=True)

    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE, related_name='produkty')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_discounted = models.BooleanField(default=False, verbose_name="Sleva")
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Zľavnená cena")
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default='ks',
        verbose_name='Jednotkové množství'
    )

    def get_final_price(self):
        if self.is_discounted and self.discount_price:
            return self.discount_price
        return self.price

    def __str__(self):
        return self.name
