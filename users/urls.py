# users/urls.py
from django.urls import path
from . import views

app_name = 'users'  # Toto je dôležité, ak chceš používať 'users:register'

urlpatterns = [
    path('register/', views.register, name='register'),
]
