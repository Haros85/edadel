from django.forms import CheckboxSelectMultiple, ModelForm
from recipe.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'image', 'tag', 'cooking_time', 'unit_of_time', 'description')
        widgets = {
            'tag': CheckboxSelectMultiple(),
        }
