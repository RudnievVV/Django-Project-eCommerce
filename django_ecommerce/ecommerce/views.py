from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def home_page(request):
    new_arrivals_list = Product.objects.filter(available=True).order_by('-created_at')[:7]
    cart_product_form = CartAddProductForm()
    return render(request, 'ecommerce/home.html', {'new_arrivals': new_arrivals_list,
                                                   'cart_product_form': cart_product_form})


def about(request):
    return render(request, 'ecommerce/about.html', {'title': 'About Us'})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category).order_by('-created_at')
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
               'cart_product_form': cart_product_form}
    return render(request, 'ecommerce/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'categories': categories, 'cart_product_form': cart_product_form}
    return render(request, 'ecommerce/product_detail.html', context)
