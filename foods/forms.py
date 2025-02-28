from django import forms
from . import models


class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.RecipeModel
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.IngredientModel
        fields = '__all__'