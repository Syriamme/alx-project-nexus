
from django.urls import path
from .views import CartListView, CartDetailView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]