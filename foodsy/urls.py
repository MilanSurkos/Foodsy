from django.contrib import admin
from django.urls import path, include
from products import views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'base.html'), name='home'),

    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('orders/', include('orders.urls')),
    path('basket/', include(('basket.urls', 'basket'), namespace='basket')),

    # 🔐 Login/Logout
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # ✅ Zapoj register view
    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('kategorie/', views.kategorie_list, name='kategorie_list'),
    path('kategoria/<int:category_id>/', views.produkty_podla_kategorie, name='produkty_podla_kategorie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
