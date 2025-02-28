from django.db import models


class RecipeModel(models.Model):
    image = models.ImageField(upload_to='recipes/', verbose_name='Загрузите фото рецепта')
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание рецепта')

    def __str__(self):
        return self.title


class IngredientModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название ингридиента')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name