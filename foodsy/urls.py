"""
URL configuration for foodsy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from products import views as product_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Domovská stránka
    path('', lambda request: render(request, 'base.html'), name='home'),

    # Aplikácie
    path('products/', include('products.urls', namespace='products')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),

    path('basket/', include('basket.urls')),

    # Produkty podľa kategórie
    path('kategorie/', product_views.kategorie_list, name='kategorie_list'),
    path('kategoria/<int:category_id>/', product_views.produkty_podla_kategorie, name='produkty_podla_kategorie'),

    # Autentifikácia
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', user_views.register, name='register'),
]

# Media súbory (napr. obrázky)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
