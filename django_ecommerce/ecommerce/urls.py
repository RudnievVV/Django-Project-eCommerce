from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='ecommerce-home'),
    path('about-us/', views.about, name='about-us'),
    path('catalog-search/<str:category_option>-<str:input_value>/', views.main_search, name='main-search'),
    path('<str:category_slug>/', views.product_list, name='product-list-by-category'),
    path('<str:category_slug>/<str:category_view>/', views.product_list_view, name='product-list-by-category-view'),
    path('product/<int:id>/<str:slug>/', views.product_detail, name='product-detail'),
]
