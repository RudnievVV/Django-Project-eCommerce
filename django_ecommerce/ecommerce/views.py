from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home_page(request):
    return render(request, 'ecommerce/home.html')


def about(request):
    return render(request, 'ecommerce/about.html', {'title': 'About Us'})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {'category': category, 'categories': categories, 'products': products, 'title': category.title}
    return render(request, 'ecommerce/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    context = {'product': product, 'categories': categories}
    return render(request, 'ecommerce/product_detail.html', context)
