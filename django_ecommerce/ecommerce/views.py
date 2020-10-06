from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse
from .services import category_defining, category_products_defining, category_products_max_price_defining, latest_products_defining, product_defining
from cart.forms import CartAddProductForm


def home_page(request):
    """rendering home page"""
    # latest products block defining: start
    latest_products = latest_products_defining()
    # latest products block defining: end
    
    # cart adding form defining: start
    cart_product_form = CartAddProductForm()
    # cart adding form defining: end
    
    return render(request, 'ecommerce/home.html', {
                                                    'title': 'Home Page',
                                                    'latest_products': latest_products,
                                                    'cart_product_form': cart_product_form,
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
    category_products_max_price = category_products_max_price_defining(category_slug)
    # category products price maximum amount defining: end

    return render(request, 'ecommerce/category.html', {
                                                        'category': category,
                                                        'category_products': category_products,
                                                        'category_products_max_price': category_products_max_price,
                                                        })


def product_page(request, sku=None):
    """rendering single product page"""
    # product defining: start
    product = product_defining(sku)
    # product defining: end

    # cart adding form defining: start
    cart_product_form = CartAddProductForm()
    # cart adding form defining: end

    # product type template defining: start
    product_template = ""
    if product.type == "Simple":
        product_template = settings.SIMPLE_PRODUCT_TEMPLATE
    else:
        raise Http404
    # product type template defining: end

    return render(request, product_template, {
                                                'product': product,
                                                'cart_product_form': cart_product_form,
                                                })
