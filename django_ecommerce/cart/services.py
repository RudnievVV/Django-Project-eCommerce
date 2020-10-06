from django.http import Http404
from itertools import chain
from ecommerce.models import SimpleProduct

def cart_products_defining(product_ids: list):
    """function to define all products related to current session"""
    result_list = chain(
        SimpleProduct.objects.filter(id__in=product_ids),
        )
    return result_list


def product_defining(product_id: id):
    """function to define product through all products models or throw 404 if no found product based on id"""
    product = chain(
            SimpleProduct.objects.filter(id=product_id),
            )
    product = list(product)
    if product:
        product = product[0] # id is unique value in DB, as result there will be only 1 found product across all products models, that's why we select first object from the list
    else:
        raise Http404

    return product