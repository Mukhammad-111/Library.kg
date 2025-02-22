from django.urls import path
from . import views


urlpatterns = [
    path('bookhouse_list/', views.BookHouseListView.as_view(), name='book_house_list'),
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list'),
    path('mashina_list/', views.MashinaListView.as_view(), name='mashina_list'),
    path('parsing_form/', views.ParsingFormView.as_view(), name='parser'),
]

