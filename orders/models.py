from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('nova', 'Nová'),
        ('zpracovani', 'Zpracování'),
        ('odeslano', 'Odesláno'),
        ('dorucena', 'Doručena'),
    ]

    PLATBA_CHOICES = [
        ('uhrazena', 'Uhrazená'),
        ('cekajici na platbu', 'Čekající na platbu'),
    ]

    DELIVERY_TIME_CHOICES = [
        ('morning', 'Ráno (8:00 - 12:00)'),
        ('afternoon', 'Odpoledne (12:00 - 18:00)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='nova')
    platba = models.CharField(max_length=50, choices=PLATBA_CHOICES, default='cekajici na platbu')
    delivery_time = models.CharField(max_length=10, choices=DELIVERY_TIME_CHOICES, default='morning')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
