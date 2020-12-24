from django import template
from django.http import QueryDict
from recipe.models import Recipe, Keyword, Follow, Favorites, Shopping

register = template.Library()


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')


@register.filter(name='get_filter_link')
def get_filter_link(request, keyword):
    new_request = request.GET.copy()
    if keyword.value in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(keyword.value)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', keyword.value)

    return new_request.urlencode()


@register.filter(name='last_recipes')
def get_filter_values(request, author_id):
    return Recipe.objects.filter(author=author_id).order_by("pub_date")[:3]


@register.filter(name='count_recipes')
def get_filter_values(request, author_id):
    recipe_count = Recipe.objects.filter(author=author_id).count() - 3
    remainder = recipe_count % 10
    if recipe_count <= 0:
        phrase = 'Страница автора'
    elif recipe_count >= 10 and recipe_count <= 20:
        phrase = f'Ещё {str(recipe_count)} рецептов'
    elif remainder == 1:
        phrase = f'Ещё {str(recipe_count)} рецепт'
    elif remainder >= 2 and remainder <= 4:
        phrase = f'Ещё {str(recipe_count)} рецепта'
    elif remainder >= 5 or remainder <= 9:
        phrase = f'Ещё {str(recipe_count)} рецептов'
    return phrase


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
    return Favorites.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_shopping')
def is_shop(recipe, user):
    return Shopping.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_follow')
def is_follow(author, user):
    return Follow.objects.filter(user=user, author=author).exists()


@register.filter(name='count_list')
def get_filter_values(request):
    counts_list = Shopping.objects.filter(user=request.user).all()
    if counts_list.count() > 0:
        return counts_list.count()
    return ''
