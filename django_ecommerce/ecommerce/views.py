from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def home_page(request):
    new_arrivals_list = Product.objects.filter(available=True).order_by('-created_at')[:7]
    cart_product_form = CartAddProductForm()
    return render(request, 'ecommerce/home.html', {'new_arrivals': new_arrivals_list,
                                                   'cart_product_form': cart_product_form,})


def about(request):
    return render(request, 'ecommerce/about.html', {'title': 'About Us'})


def product_list(request, category_slug=None, pagination_sort_by="title", pagination_show=12):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()

    if request.session.get('pagination_sort_by') is not None and request.session.get('pagination_show') is not None:
        pagination_sort_by = request.session.get('pagination_sort_by')
        pagination_show = request.session.get('pagination_show')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        if request.method == "POST":
            pagination_sort_by = request.POST.get('pagination-sortby-select-dropdown')
            pagination_show = int(request.POST.get('pagination-show-select-dropdown'))
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show)
        else:
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
               'cart_product_form': cart_product_form, 'products_count': products_count,
               'pagination_sort_by': pagination_sort_by, 'pagination_show': pagination_show}

    request.session['pagination_sort_by'] = pagination_sort_by
    request.session['pagination_show'] = pagination_show
    return render(request, 'ecommerce/product_list_grid.html', context)


def product_list_view(request, category_slug, category_view):
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    if category_view == 'grid':
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category).order_by('title')
        products_count = products.count
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        products = paginator.get_page(page)

        context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
                   'cart_product_form': cart_product_form, 'products_count': products_count}
        return render(request, 'ecommerce/product_list_grid.html', context)

    if category_view == 'list':
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category).order_by('title')
        products_count = products.count
        paginator = Paginator(products, 5)
        page = request.GET.get('page')
        products = paginator.get_page(page)

        context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
                   'cart_product_form': cart_product_form, 'products_count': products_count}
        return render(request, 'ecommerce/product_list_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'categories': categories, 'cart_product_form': cart_product_form}
    return render(request, 'ecommerce/product_detail.html', context)


def main_search(request, category_option, input_value):
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    if category_option != "All Categories":
        products = Product.objects.filter(Q(category=Category.objects.get(title=category_option)),
                                          Q(title__icontains=input_value.strip())).order_by('title')
    else:
        products = Product.objects.filter(title__icontains=input_value.strip()).order_by('title')
    paginator = Paginator(products, 12)
    products_count = products.count
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {'products': products, 'categories': categories, 'products_count': products_count,
               'cart_product_form': cart_product_form, 'title': 'Search Result'}
    return render(request, 'ecommerce/main_search.html', context=context)
