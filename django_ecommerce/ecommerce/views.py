from django.shortcuts import render
from .services import category_defining, latest_products_defining


def home_page(request):
    """rendering home page"""
    # latest products block defining: start
    latest_products = latest_products_defining()
    # latest products block defining: end
    
    return render(request, 'ecommerce/home.html', {
                                                    'title': 'Home Page',
                                                    'latest_products': latest_products,
                                                    })


def category_page(request, category_slug=None):
    """rendering category page w/ or w/o products inside"""
    # category defining: start 
    category = category_defining(category_slug)
    # category defining: end


def product_detail(request, sku=None):
    """rendering single product page"""
    pass
