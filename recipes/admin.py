from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1               # сколько пустых форм показывать по умолчанию
    min_num = 0
    can_delete = True

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'servings')  # колонки в списке
    list_filter = ('created',)                        # фильтры справа
    search_fields = ('title', 'description')          # строка поиска
    inlines = [IngredientInline]                      # показываем ингредиенты прямо на форме рецепта

# Если хотите, можете отдельно зарегистрировать Ingredient,
# но это не обязательно, т.к. мы работаём с ними inline.
# admin.site.register(Ingredient)
