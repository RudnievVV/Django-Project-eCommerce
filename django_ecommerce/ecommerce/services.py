from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Category, SimpleProduct
from itertools import chain
from math import ceil


def category_defining(category_slug: str):
    """function to define category or throw 404 if no found category"""

    return get_object_or_404(Category, slug=category_slug)


def category_products_defining(category_slug: str):
    """function to define all category's products"""
    category = category_defining(category_slug)
    result_list = chain(
        SimpleProduct.objects.filter(category=category),
        )

    return result_list


def category_products_max_price_defining(category_slug: str):
    """function to define max products price of category"""
    category = category_defining(category_slug)
    if category.products_inside():
        max_category_products_price = ceil(
            sorted(
                chain(
                    SimpleProduct.objects.filter(category=category).order_by('price')[:1],
                    ),
                key=lambda product: product.price, reverse=True)[0].price.amount
                )
    else:
         max_category_products_price = 0

    return str(max_category_products_price)


def latest_products_defining(latest_products_count=settings.LATEST_PRODUCTS_COUNT):
    """function to define latest added products based on settings quantity"""
    result_list = sorted(
        chain(
            SimpleProduct.objects.order_by('-created_at')[:latest_products_count],
            ),
        key=lambda product: product.created_at, reverse=True)
        
    return result_list[:latest_products_count]