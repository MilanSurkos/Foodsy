from django.shortcuts import render

def recipe_list(request):
    return render(request, 'recipes/recipe_list.html')
