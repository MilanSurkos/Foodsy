from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe-list'),
    path('add/', views.RecipeCreateView.as_view(), name='recipe-add'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    ]