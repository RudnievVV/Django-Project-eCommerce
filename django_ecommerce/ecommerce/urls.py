from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home_page, name='ecommerce-home'),
    path('about-us/', views.about, name='about-us'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product-list-by-category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product-detail'),
]