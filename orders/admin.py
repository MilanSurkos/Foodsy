from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)