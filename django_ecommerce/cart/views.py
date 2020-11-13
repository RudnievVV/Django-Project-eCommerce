from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.conf import settings
from ecommerce.services import product_defining
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_sku):
    """adding product to user session"""
    # defining variables that will be used to add product: start
    cart = Cart(request)
    product = product_defining(product_sku)
    form = CartAddProductForm(request.POST)
    # defining variables that will be used to add product: end
    
    # adding product to user session: start
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, f'{product} has been successfully added to your cart!')
    # adding product to user session: end

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_sku):
    """removing product from user session"""
    # defining variables that will be used to remove product: start
    cart = Cart(request)
    product = product_defining(product_sku)
    # defining variables that will be used to remove product: end

    # removing product from user session: start
    cart.remove(product)
    messages.success(request, f'{product} has been successfully removed from your cart!')
    # removing product from user session: end

    # checking if user's previous page exists, because url can be directly opened
    if request.META['HTTP_REFERER'] is None:
        return redirect('ecommerce-home')

    return redirect(request.META['HTTP_REFERER'])