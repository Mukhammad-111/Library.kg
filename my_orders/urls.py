from django.urls import path
from . import views


urlpatterns = [
    path('cart_list/', views.CartListView.as_view(), name='cart_list'),
    path('cart_list/<int:id>/delete/', views.DeleteCartView.as_view(), name='delete_cart'),
    path('cart_list/<int:id>/update/', views.UpdateCartView.as_view(), name='update_cart'),
    path('cart_list/<int:id>/order/', views.OrderCartView.as_view(), name='order_cart'),
    path('create_cart/', views.CreateCartView.as_view(), name='create_cart'),
]

