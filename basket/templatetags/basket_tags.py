from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None

@register.filter
def get_total_quantity(basket):
    if isinstance(basket, dict):
        return sum(basket.values())
    return 0