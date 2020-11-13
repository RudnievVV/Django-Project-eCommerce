from django.urls import path
from . import views


urlpatterns = [
    path('add/<str:product_sku>/', views.cart_add, name='cart-add'),
    path('remove/<str:product_sku>/', views.cart_remove, name='cart-remove'),
]
