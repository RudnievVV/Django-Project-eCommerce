from django.shortcuts import render
from .services import category_defining, category_products_defining, category_product_max_price_defining, latest_products_defining


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
    # category products defining: start
    category_products = category_products_defining(category_slug)
    # category products defining: end
    # category products price maximum amount defining: start
    category_product_max_price = category_product_max_price_defining(category_slug)
    # category products price maximum amount defining: end

    return render(request, 'ecommerce/category.html', {
                                                        'category': category,
                                                        'category_products': category_products,
                                                        'category_product_max_price': category_product_max_price,
                                                        })


def product_detail(request, sku=None):
    """rendering single product page"""
    pass
