from django.contrib import admin
from django.urls import path, include
from products import views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Domovská stránka, môžeš mať aj vlastnú view funkciu namiesto lambda
    path('', lambda request: render(request, 'base.html'), name='home'),

    # Produkty s namespace 'products'
    path('products/', include(('products.urls', 'products'), namespace='products')),

    # Objednávky, bez namespace (ak si nedefinoval v orders/urls.py app_name, nechaj tak)
    path('orders/', include('orders.urls')),

    # Basket s namespace 'basket' (dôležité!)
    path('basket/', include(('basket.urls', 'basket'), namespace='basket')),

    # Kategórie - ak toto používaš mimo namespace products
    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('kategoria/<int:category_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)