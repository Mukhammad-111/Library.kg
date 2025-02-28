from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class RecipesListView(generic.ListView):
    template_name = 'foods/recipe_list.html'
    context_object_name = 'recipes'
    model = models.RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RecipesDetailView(generic.DetailView):
    template_name = 'foods/recipe_detail.html'
    context_object_name = 'recipe_id'
    model = models.RecipeModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context


class IngredientListView(generic.ListView):
    template_name = 'foods/ingredient_list.html'
    context_object_name = 'ingredients'
    model = models.IngredientModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CreateRecipesView(generic.CreateView):
    template_name = 'foods/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipesView, self).form_valid(form=form)


class DeleteRecipesView(generic.DeleteView):
    template_name = 'foods/delete_recipe.html'
    success_url = '/recipe_list/'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)


class BrowseRecipesView(generic.UpdateView):
    template_name = 'foods/browse_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_list/'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BrowseRecipesView, self).form_valid(form=form)


class CreateIngredientView(generic.CreateView):
    template_name = 'foods/create_ingredient.html'
    form_class = forms.IngredientForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateIngredientView, self).form_valid(form=form)

class DeleteIngredientView(generic.DeleteView):
    template_name = 'foods/delete_ingredient.html'
    success_url = 'recipe_list'

    def get_object(self, *args, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(models.IngredientModel, id=ingredient_id)