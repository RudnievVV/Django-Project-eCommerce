from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='ecommerce-home'),
    path('about-us/', views.about, name='about-us'),
]