from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_discounted', 'discount_price', 'unit')
    fields = ('name', 'price', 'is_discounted', 'discount_price', 'unit', 'description', 'image', 'category')
