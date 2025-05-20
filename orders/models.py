from django.db import models

# Create your models here.


from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[('new', 'New'), ('fulfilled', 'Fulfilled')],
        default='new'
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)