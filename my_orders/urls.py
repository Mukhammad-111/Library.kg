from django.urls import path
from . import views


urlpatterns = [
    path('cart_list/', views.cart_list_view, name='cart_list'),
    path('cart_list/<int:id>/delete/', views.delete_cart_view, name='delete_cart'),
    path('cart_list/<int:id>/update/', views.update_cart_view, name='update_cart'),
    path('cart_list/<int:id>/order/', views.order_cart_view, name='order_cart'),
    path('create_cart/', views.create_cart_view, name='create_cart'),
]