from django.http import Http404
from itertools import chain
from ecommerce.models import SimpleProduct

def cart_products_defining(product_ids: list):
    """function to define all products related to current session"""
    result_list = chain(
        SimpleProduct.objects.filter(id__in=product_ids),
        )
    return result_list