from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='ecommerce-home'),
    path('<str:category_slug>/', views.category_page, name='category-page'),
    path('product/<str:sku>/', views.product_page, name='product-page'),
]
