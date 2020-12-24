import json
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from recipe.models import Recipe, Ingredient, AmountIngredients, User, Follow, Favorites, Shopping


def get_ingredients(request):
    query = str(request.GET.get("query")).lower()
    ingredients = Ingredient.objects.filter(
        title__contains=query).values("title", "unit")
    return JsonResponse(list(ingredients), safe=False)


@login_required
def follow(request):
    follow_pk = int(json.loads(request.body).get('id'))
    if request.user.id != follow_pk:
        created = Follow.objects.get_or_create(
            user_id=request.user.id, author_id=follow_pk)
    return JsonResponse({'success': True}) if created else JsonResponse({'success': False})


@login_required
def unfollow(request, follow_pk):
    deleted = Follow.objects.get(user_id=request.user.id, author_id=follow_pk)
    deleted.delete()
    return JsonResponse({'success': True}) if deleted else JsonResponse({'success': False})


@login_required
def in_favor(request):
    favor_pk = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, id=favor_pk)
    Favorites.objects.get_or_create(user=request.user, recipe=recipe)
    return JsonResponse({'success': True})


@login_required
def out_favor(request, favor_pk):
    recipe = get_object_or_404(Recipe, id=favor_pk)
    user = get_object_or_404(User, username=request.user.username)
    deleted = get_object_or_404(Favorites, user=user, recipe=recipe)
    deleted.delete()
    return JsonResponse({'success': True})


@login_required
def in_list(request):
    purch_pk = int(json.loads(request.body).get('id'))
    recipe = get_object_or_404(Recipe, id=purch_pk)
    Shopping.objects.get_or_create(user=request.user, recipe=recipe)
    return JsonResponse({'success': True})


@login_required
def out_list(request, purch_pk):
    recipe = get_object_or_404(Recipe, id=purch_pk)
    user = get_object_or_404(User, username=request.user.username)
    deleted = get_object_or_404(Shopping, user=user, recipe=recipe)
    deleted.delete()
    return JsonResponse({'success': True})


@login_required
def download(request):
    shop_list = Shopping.objects.filter(
        user_id=request.user.id).values_list("recipe", flat=True).all()
    ing_list = AmountIngredients.objects.filter(
        recipe_id__in=shop_list).order_by('ingredient')

    out_list = {}
    for value in ing_list:
        if not value.ingredient in out_list.keys():
            out_list[value.ingredient] = value.amount
        else:
            out_list[value.ingredient] += value.amount

    my_list = []
    zero = []
    my_list.append('Примерный список покупок:')
    my_list.append('\n\n')
    for key, val in out_list.items():
        if val == 0:
            zero.append(f'[ ] {key.title} \n')
        else:
            my_list.append(f'[ ] {key.title} - {val} {key.unit} \n')
    my_list.append('\n')
    if len(zero) != 0:
        my_list.append('Не забудьте докупить:\n')
        for value in zero:
            my_list.append(value)
    my_list.append('\n')
    my_list.append('Приятного аппетита!')

    response = HttpResponse(my_list, 'Content-Type: text/plain')
    response['Content-Disposition'] = 'attachment; filename="shop_list.txt"'
    return response


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(
        request,
        "misc/500.html",
        status=500
    )
