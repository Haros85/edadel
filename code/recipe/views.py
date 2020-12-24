from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import (
    Recipe,
    Ingredient,
    AmountIngredients,
    Time,
    Keyword,
    User,
    Follow,
    Shopping,
)

from .forms import RecipeForm
from .utils import get_ingredients_list, get_tags_for_edit
from pathlib import Path
import os


def index(request):
    tag = request.GET.getlist('filters')
    recipe_list = Recipe.objects.all()
    if tag:
        recipe_list = recipe_list.filter(tag__value__in=tag).distinct().all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator, }
    )


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    tag = request.GET.getlist('filters')
    recipe_list = Recipe.objects.filter(author=profile.pk).all()
    if tag:
        recipe_list = recipe_list.filter(tag__value__in=tag)
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'profile.html',
        {
            'profile': profile,
            'recipe_list': recipe_list,
            'page': page,
            'paginator': paginator
        }
    )


def recipe_view(request, slug, username):
    recipe = get_object_or_404(Recipe, slug=slug)
    profile = get_object_or_404(User, username=username)
    return render(
        request,
        'recipe.html',
        {'profile': profile, 'recipe': recipe, }
    )


@login_required
def new_recipe(request):
    user = User.objects.get(username=request.user)
    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None)
    if request.method == 'POST':
        ingredients = get_ingredients_list(request)
        if not ingredients:
            form.add_error(None, 'Добавьте ингредиенты')
        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = user
            recipe.save()
            for ing_title, amount in ingredients.items():
                ingredient = get_object_or_404(Ingredient, title=ing_title)
                recipe_ing = AmountIngredients(
                    recipe=recipe,
                    ingredient=ingredient,
                    amount=amount
                )
                recipe_ing.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'new_recipe.html', {'form': form})


@login_required
def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user != recipe.author:
        return redirect('recipe', slug=slug)

    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )
    if request.method == "POST":
        ingredients = get_ingredients_list(request)
        if not ingredients:
            form.add_error(None, 'Добавьте ингредиенты')
        if form.is_valid():
            form.save()
            AmountIngredients.objects.filter(recipe=recipe).delete()

            for ing_title, amount in ingredients.items():
                ingredient = get_object_or_404(Ingredient, title=ing_title)
                recipe_ing = AmountIngredients(
                    recipe=recipe,
                    ingredient=ingredient,
                    amount=amount
                )
                recipe_ing.save()
            return redirect('recipe_view', username=request.user.username, slug=recipe.slug)

    all_tags = recipe.tag.values_list('value', flat=True)
    all_ingredients = AmountIngredients.objects.filter(recipe=recipe.id)

    return render(request, 'change_recipe.html', {
        'form': form,
        'recipe': recipe,
        'all_tags': all_tags,
        'all_ingredients': all_ingredients,
    })


@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    path = str(recipe.image)
    os.remove(f'{Path(__file__).resolve(strict=True).parent.parent}/media/{path}')
    recipe.delete()
    return redirect("index")


@login_required
def follow(request, username):
    author = get_object_or_404(User, username=username)
    user = get_object_or_404(User, username=request.user)
    follow_count = Follow.objects.filter(user=request.user, author=author).count()
    if user != author and follow_count == 0:
        Follow.objects.create(user=user, author=author)
        return redirect('profile', username=username)
    return redirect('profile', username=username)


@login_required
def follow_view(request):
    follow = Follow.objects.filter(user=request.user).order_by("author").all()
    paginator = Paginator(follow, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "follow.html", {"page": page, "paginator": paginator})


@login_required
def favor_view(request):
    tag = request.GET.getlist('filters')
    recipe_list = Recipe.objects.filter(
        favor__user__id=request.user.id).all()
    if tag:
        recipe_list = recipe_list.filter(tag__value__in=tag).distinct().all()

    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'favorites.html', {
        'page': page,
        'paginator': paginator,
    })


@login_required
def shop_list(request):
    shop_list = Shopping.objects.filter(user=request.user).all()

    return render(request, 'shop_list.html', {
        'page': shop_list,
    })
