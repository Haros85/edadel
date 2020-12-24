from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Keyword

User = get_user_model()


def get_ingredients_list(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            ing_number = key[15:]
            ingredients[request.POST[key]] = request.POST[f'valueIngredient_{ing_number}']
    return ingredients


def get_tags_for_edit(request):
    data = request.POST.copy()
    values = Keyword.objects.values_list('value')
    tags = []
    for value in values:
        if value in data and data.get(value) == 'on':
            tag = get_object_or_404(Tags, value=value)
            tags.append(tag)

    return tags
