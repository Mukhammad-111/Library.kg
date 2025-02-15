from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('create_review/', views.create_review_view, name="create_review"),


    path("about_me/", views.about_me, name="about_me"),
    path("text_and_photo/", views.text_and_photo, name="text_and_photo"),
    path("system_time/", views.system_time, name="system_time"),
]