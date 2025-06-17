from django.urls import path
from . import views

app_name = 'discounts'

urlpatterns = [
    path('', views.discount_list, name='slevy'),
]