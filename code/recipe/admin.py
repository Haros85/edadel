from django.contrib import admin

from .models import AmountIngredients, Ingredient, Keyword, Recipe, Time


class AmountInLine(admin.TabularInline):
    model = AmountIngredients
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "author", "pub_date")
    search_fields = ("title",)
    list_filter = ("title",)
    inlines = (AmountInLine,)


class KeywordAdmin(admin.ModelAdmin):
    list_display = ("pk", "value", "title")
    empty_value_display = "-пусто-"


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "unit")
    search_fields = ("title",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


class TimeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "unit",
        "reduction",
    )
    search_fields = ("unit",)


class AmountIngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "amount",
        "ingredient",
        "recipe",
    )
    search_fields = ("recipe",)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(AmountIngredients, AmountIngredientsAdmin)
