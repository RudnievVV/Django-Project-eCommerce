from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ecommerce.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        messages.success(request, f'{product} has been successfully added to your cart!')
    if request.META['HTTP_REFERER'] is None:
        return redirect('ecommerce-home')
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product} has been successfully removed from your cart!')
    if request.META['HTTP_REFERER'] is None:
        return redirect('ecommerce-home')
    return redirect(request.META['HTTP_REFERER'])


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})