# Foodsy
Foodsy
 -[x] 1.Vytvorenie priečinka pre projekt Foodsy :
django-admin startproject Foodsy
- [x] 2.Spustenie vývojového servera :
python manage.py runserver
- [x] 3.Vytvorenie aplikácií (modulov)
- [x] 3a.Vytvor aplikácie pomocou súboru manage.py:
python manage.py startapp products
python manage.py startapp users
python manage.py startapp orders
python manage.py startapp basket
- [x] 3b.Zaregistruj aplikácie v settings.py :
  - Otvor Foodsy/settings.py a na koniec zoznamu INSTALLED_APPS pridaj:
INSTALLED_APPS = [
...
'products',
'users',
'orders',
'basket',
]
- [x] 3c. Spustenie základných migrácií :
python manage.py migrate
- [x] 3d. Vytvorenie superužívateľa :
python manage.py createsuperuser
  - Systém ťa vyzve na zadanie mena, e-mailu a hesla
- [x] 3e. Opätovné spustenie servera :
python manage.py runserver
- [x] 4.Vytvorenie hlavných modelov
- [x] 4a. Model Kategorie (v products/models.py):
from django.db import models
class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)
    rodic = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='potomci'
    )
    def __str__(self):
        return self.nazev
- [x] 4b. Model Product (pokračovanie v products/models.py):
class Product(models.Model):
    PRODUCT_TYPES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True)
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    available = models.BooleanField(default=True)
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
- [ ] 4c.Model User (v users/models.py):
  - Najprv importuj: 
from django.contrib.auth.models import AbstractUser
from django.db import models
  - Potom vytvor model:
class User(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrator'),
        ('USER', 'User')
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='USER')
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    preferred_channel = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('mail', 'Mail')],
        default='email'
    )
- [ ] 4d.Nastavenie vlastného používateľa v settings.py :
    - V Foodsy/settings.py pridaj:
AUTH_USER_MODEL = 'users.User'
- [ ] 4e. Modely Order a OrderItem (v orders/models.py) :

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

- [ ] 5.Vygeneruj a aplikuj migrácie 
- [ ] 5a.Vytvorenie migrácií :
python manage.py makemigrations
- [ ] 5b.Aplikovanie migrácií :
python manage.py migrate
- [ ] 6.Prepojenie modelov s admin rozhraním 
- [ ] 6a.Zaregistruj modely v admin súboroch jednotlivých aplikácií: 
    - products/admin.py :
from django.contrib import admin
from .models import Kategorie, Product

admin.site.register(Kategorie)
admin.site.register(Product)
    - users/admin.py :
from django.contrib import admin
from .models import User
admin.site.register(User)
    - orders/admin.py :
from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

- [ ] 7b.Vytvor jednoduchý pohľad (view) :
    - products/views.py :
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})
- [ ] 8.Pridaj URL adresy do hlavného súboru Foodsy/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    # môžeš pridať aj users, orders, basket...
]
- [ ] 9.Vytvor základné HTML šablóny
- [ ] 9a.Vytvor priečinok templates/products/ a v ňom súbor index.html:
    - products/templates/products/index.html :

<!DOCTYPE html>
<html>
<head>
    <title>Foodsy - Produkty</title>
</head>
<body>
    <h1>Produkty</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} – {{ product.price }} €</li>
        {% empty %}
            <li>Žiadne produkty.</li>
        {% endfor %}
    </ul>
</body>
</html>
- [ ] 9b.V settings.py pridaj cestu k šablónam (ak ešte nie je) :
import os

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
- [ ] 10.Spustenie a kontrola
- [ ] 10a.Spusti vývojový server :
python manage.py runserver
- [ ] 10b.Otvor v prehliadači:
Admin rozhranie: http://127.0.0.1:8000/admin

Produkty: http://127.0.0.1:8000/products/