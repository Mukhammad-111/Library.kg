from django.contrib import admin
from . import models

admin.site.register(models.RecipeModel)
admin.site.register(models.IngredientModel)
