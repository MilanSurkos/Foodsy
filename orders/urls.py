from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders'),  # <-- this name is what you're referencing
]
