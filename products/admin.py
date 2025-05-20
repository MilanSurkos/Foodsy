from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Kategorie, Product

admin.site.register(Kategorie)
admin.site.register(Product)