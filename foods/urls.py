from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipesListView.as_view(), name='recipe_list'),
    path('recipe_detail/<int:id>/', views.RecipesDetailView.as_view(), name='recipe_detail'),

    path('recipe_list/create/', views.CreateRecipesView.as_view(), name='create_recipe'),
    path('recipe_list/<int:id>/browse/', views.BrowseRecipesView.as_view(), name='browse_recipe'),
    path('recipe_list/<int:id>/delete/', views.DeleteRecipesView.as_view(), name='delete_recipe'),

    path('ingredient_list/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('recipe_list/<int:recipe_id>/create_ingredient/', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredient_list/<int:id>/delete/', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
]
