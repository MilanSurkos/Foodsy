from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from foodsy.views import home  # Import the home view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),  # Use the home view

    # Include app URLs with namespaces
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('basket/', include(('basket.urls', 'basket'), namespace='basket')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    # path('recipes/', include(('recipes.urls', 'recipes'), namespace='recipes')),  # Include recipes app URLs
    path('discounts/', include(('discounts.urls', 'discounts'), namespace='discounts')),  # Include discounts app URLs

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    #spravce
    path('products/', include('products.urls')),
    path('recipes/', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)