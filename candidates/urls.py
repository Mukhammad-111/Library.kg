from django.urls import path
from . import views


app_name = 'applicants'


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('applicant_list/', views.ApplicantListView.as_view(), name='applicant_list')
]