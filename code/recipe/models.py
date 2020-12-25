from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Keyword(models.Model):
    title = models.CharField("Ключевое слово", max_length=10)
    value = models.CharField("Значение тега", max_length=10)
    color = models.CharField("Цвет", max_length=10, null=True)

    class Meta:
        verbose_name = u"Тег"
        verbose_name_plural = u"Теги"
        ordering = ["pk"]

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(
        "Название ингредиента", max_length=100, null=True, blank=True
    )
    unit = models.CharField("Еденица измерения", max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = u"Ингредиент"
        verbose_name_plural = u"Ингредиенты"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Time(models.Model):
    unit = models.CharField(max_length=10, verbose_name=u"Еденица измерения")
    reduction = models.CharField(max_length=5, verbose_name=u"Сокращение")

    class Meta:
        verbose_name = u"Время"
        verbose_name_plural = u"Время"
        ordering = ["pk"]

    def __str__(self):
        return self.reduction


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cook", verbose_name=u"Автор"
    )
    title = models.CharField("Название рецепта", max_length=100)
    image = models.ImageField(upload_to="recipes/")
    description = models.TextField("Описание")
    ingredient = models.ManyToManyField(
        Ingredient, through="AmountIngredients", through_fields=("recipe", "ingredient")
    )
    tag = models.ManyToManyField(Keyword, verbose_name=u"Теги")
    cooking_time = models.IntegerField("Время приготовления")
    unit_of_time = models.ForeignKey(
        Time,
        on_delete=models.CASCADE,
        related_name="unit_of_time",
        verbose_name=u"Еденица времени",
    )
    slug = models.SlugField("Ссылка", unique=True)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = u"Рецепт"
        verbose_name_plural = u"Рецепты"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title


class AmountIngredients(models.Model):
    amount = models.IntegerField("Дозировка")
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredient",
        verbose_name=u"Ингредиент",
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name=u"Блюдо")

    class Meta:
        verbose_name = u"Дозировка"
        verbose_name_plural = u"Дозировка"
        ordering = ["recipe", "pk"]

    def __str__(self):
        return self.ingredient.unit


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favor_by")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favor")

    def __str__(self):
        return self.recipe.title


class Shopping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shopper")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="for_list"
    )

    def __str__(self):
        return self.recipe.title
