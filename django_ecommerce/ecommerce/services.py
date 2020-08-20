from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Category, SimpleProduct
from itertools import chain


def category_defining(category_slug: str):

    return get_object_or_404(Category, slug=category_slug)


def latest_products_defining(latest_products_count=settings.LATEST_PRODUCTS_COUNT):
    result_list = sorted(
        chain(SimpleProduct.objects.order_by('-created_at')[:latest_products_count]),
        key=lambda product: product.created_at, reverse=True)
        
    return result_list[:latest_products_count]