from .cart import Cart
from ecommerce.models import Product


def cart(request):
    product_ids = Cart(request).cart.keys()
    cart_products = Product.objects.filter(id__in=product_ids)
    return {'cart': Cart(request), 'cart_products': cart_products}
