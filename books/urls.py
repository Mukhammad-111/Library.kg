from django.urls import path
from . import views


urlpatterns = [
    path("about_me/", views.about_me, name="about_me"),
    path("text_and_photo/", views.text_and_photo, name="text_and_photo"),
    path("system_time/", views.system_time, name="system_time"),
]