from .cart import Cart
from .services import cart_products_defining


def cart(request):
    product_ids = Cart(request).cart.keys()
    cart_products = cart_products_defining(product_ids)
    return {'cart': Cart(request), 'cart_products': cart_products}
