from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 'description', 'servings',
            'instructions',
        ]

# здесь мы получаем FormSet для Ingredient
IngredientFormSet = inlineformset_factory(
    parent_model=Recipe,
    model=Ingredient,
    fields=('name', 'quantity'),
    extra=1,
    can_delete=True
)