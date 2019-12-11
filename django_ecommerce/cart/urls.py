from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart-detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart-add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart-remove'),
]
