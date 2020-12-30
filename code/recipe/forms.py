from django.forms import CheckboxSelectMultiple, ModelForm
from django.core.exceptions import ValidationError
from recipe.models import Recipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'tag', 'cooking_time', 'unit_of_time', 'description')
        widgets = {
            'tag': CheckboxSelectMultiple(),
        }

    def clean(self):
        known_ids = []
        for items in self.data.keys():
            if 'nameIngredient' in items:
                name, id = items.split('_')
                known_ids.append(id)
        for id in known_ids:
            title = self.data.get(f'nameIngredient_{id}'),
            unit = self.data.get(f'unitsIngredient_{id}')
            ingredient_exists = Ingredient.objects.filter(
                title=title[0],
                unit=unit,
            ).exists()
            if not ingredient_exists:
                raise ValidationError('Выберите ингредиент из списка!')