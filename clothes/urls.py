from django.urls import path
from . import views


urlpatterns = [
    path('all_clothes/', views.ClothesListView.as_view(), name='all_clothes'),
    path('children_clothes/', views.ChildrenClothesView.as_view(), name='children_clothes'),
    path('teenage_clothes/', views.TeenageClothesView.as_view(), name='teenage_clothes'),
    path('adult_clothes/', views.AdultClothesView.as_view(), name='adult_clothes'),
]