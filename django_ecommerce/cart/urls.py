from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart-detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart-add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart-remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-<str:guest_order>/', views.checkout, name='checkout-guest'),
]
