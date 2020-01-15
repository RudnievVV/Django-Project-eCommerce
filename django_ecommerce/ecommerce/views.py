from django.db.models import Q
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


def product_list(request, category_slug=None, pagination_sort_by="title", pagination_show_grid=12):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()

    if request.session.get('pagination_sort_by') is not None and request.session.get('pagination_show_grid') is not None:
        pagination_sort_by = request.session.get('pagination_sort_by')
        pagination_show_grid = request.session.get('pagination_show_grid')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        max_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('-price').first().price.__str__()[1:].split(','))) + 1)
        min_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('price').first().price.__str__()[1:].split(','))))

        if request.method == "POST" and request.POST.get('slider-price-min-value') is not None and \
                request.POST.get('slider-price-max-value') is not None:
            slider_price_min_value = request.POST.get('slider-price-min-value')
            slider_price_max_value = request.POST.get('slider-price-max-value')
        else:
            if request.session.get(category.title) is not None and \
                    request.session.get(category.title).get('slider_price_min_value') is not None and \
                    request.session.get(category.title).get('slider_price_max_value') is not None:
                slider_price_min_value = request.session[category.title]['slider_price_min_value']
                slider_price_max_value = request.session[category.title]['slider_price_max_value']
            else:
                slider_price_min_value = min_product_price
                slider_price_max_value = max_product_price

        if request.method == "POST" and \
                request.POST.get('pagination-sortby-select-dropdown') is not None and \
                request.POST.get('pagination-showgrid-select-dropdown') is not None:
            pagination_sort_by = request.POST.get('pagination-sortby-select-dropdown')
            pagination_show_grid = int(request.POST.get('pagination-showgrid-select-dropdown'))
            products = Product.objects.filter(Q(category=category),
                                              Q(price__range=[slider_price_min_value,
                                                              slider_price_max_value])).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_grid)
        else:
            products = Product.objects.filter(Q(category=category),
                                              Q(price__range=[slider_price_min_value,
                                                              slider_price_max_value])).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_grid)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
               'cart_product_form': cart_product_form, 'products_count': products_count,
               'pagination_sort_by': pagination_sort_by, 'pagination_show_grid': pagination_show_grid,
               'min_product_price': min_product_price, 'max_product_price': max_product_price,
               'slider_price_min_value': int(slider_price_min_value), 'slider_price_max_value': int(slider_price_max_value)}

    request.session.setdefault(category.title, {})
    request.session[category.title]['slider_price_min_value'] = slider_price_min_value
    request.session[category.title]['slider_price_max_value'] = slider_price_max_value
    request.session['pagination_sort_by'] = pagination_sort_by
    request.session['pagination_show_grid'] = pagination_show_grid
    return render(request, 'ecommerce/product_list_grid.html', context)


def product_list_view(request, category_slug, category_view, pagination_sort_by="title", pagination_show_grid=12,
                      pagination_show_list=5):
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    if category_view == 'grid':
        category = get_object_or_404(Category, slug=category_slug)

        if request.session.get('pagination_sort_by') is not None and request.session.get('pagination_show_grid') is not None:
            pagination_sort_by = request.session.get('pagination_sort_by')
            pagination_show_grid = request.session.get('pagination_show_grid')

        if request.method == "POST":
            pagination_sort_by = request.POST.get('pagination-sortby-select-dropdown')
            pagination_show_grid = int(request.POST.get('pagination-showgrid-select-dropdown'))
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_grid)
        else:
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_grid)

        page = request.GET.get('page')
        products = paginator.get_page(page)

        max_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('-price').first().price.__str__()[1:].split(','))) + 1)
        min_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('price').first().price.__str__()[1:].split(','))))

        context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
                   'cart_product_form': cart_product_form, 'products_count': products_count,
                   'pagination_sort_by': pagination_sort_by, 'pagination_show_grid': pagination_show_grid,
                   'min_product_price': min_product_price, 'max_product_price': max_product_price}

        request.session['pagination_sort_by'] = pagination_sort_by
        request.session['pagination_show_grid'] = pagination_show_grid
        return render(request, 'ecommerce/product_list_grid.html', context)

    if category_view == 'list':
        category = get_object_or_404(Category, slug=category_slug)

        if request.session.get('pagination_sort_by') is not None and request.session.get('pagination_show_list') is not None:
            pagination_sort_by = request.session.get('pagination_sort_by')
            pagination_show_list = request.session.get('pagination_show_list')

        if request.method == "POST":
            pagination_sort_by = request.POST.get('pagination-sortby-select-dropdown')
            pagination_show_list = int(request.POST.get('pagination-showlist-select-dropdown'))
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_list)
        else:
            products = Product.objects.filter(category=category).order_by(pagination_sort_by)
            products_count = products.count
            paginator = Paginator(products, pagination_show_list)

        page = request.GET.get('page')
        products = paginator.get_page(page)

        max_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('-price').first().price.__str__()[1:].split(','))) + 1)
        min_product_price = int(float(''.join(
            Product.objects.filter(category=category).order_by('price').first().price.__str__()[1:].split(','))))

        context = {'category': category, 'categories': categories, 'products': products, 'title': category.title,
                   'cart_product_form': cart_product_form, 'products_count': products_count,
                   'pagination_sort_by': pagination_sort_by, 'pagination_show_list': pagination_show_list,
                   'min_product_price': min_product_price, 'max_product_price': max_product_price}

        request.session['pagination_sort_by'] = pagination_sort_by
        request.session['pagination_show_list'] = pagination_show_list
        return render(request, 'ecommerce/product_list_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'categories': categories, 'cart_product_form': cart_product_form}
    return render(request, 'ecommerce/product_detail.html', context)


def main_search(request, category_option, input_value, pagination_sort_by="title", pagination_show_grid=12):
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()

    if request.session.get('pagination_sort_by') is not None and request.session.get('pagination_show_grid') is not None:
        pagination_sort_by = request.session.get('pagination_sort_by')
        pagination_show_grid = request.session.get('pagination_show_grid')

    if category_option != "All Categories":
        products = Product.objects.filter(Q(category=Category.objects.get(title=category_option)),
                                          Q(title__icontains=input_value.strip())).order_by(pagination_sort_by)
        max_product_price = int(float(''.join(
            Product.objects.filter(category=Category.objects.get(
                title=category_option)).order_by('-price').first().price.__str__()[1:].split(','))) + 1)
        min_product_price = int(float(''.join(
            Product.objects.filter(category=Category.objects.get(
                title=category_option)).order_by('price').first().price.__str__()[1:].split(','))))
    else:
        products = Product.objects.filter(title__icontains=input_value.strip()).order_by(pagination_sort_by)
        max_product_price = int(float(''.join(
            Product.objects.all().order_by('-price').first().price.__str__()[1:].split(','))) + 1)
        min_product_price = int(float(''.join(
            Product.objects.all().order_by('price').first().price.__str__()[1:].split(','))))

    if request.method == "POST":
        pagination_sort_by = request.POST.get('pagination-sortby-select-dropdown')
        pagination_show_grid = int(request.POST.get('pagination-showgrid-select-dropdown'))
        products_count = products.count
        paginator = Paginator(products, pagination_show_grid)
    else:
        products_count = products.count
        paginator = Paginator(products, pagination_show_grid)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {'products': products, 'categories': categories, 'products_count': products_count,
               'cart_product_form': cart_product_form, 'title': 'Search Result',
               'pagination_sort_by': pagination_sort_by, 'pagination_show_grid': pagination_show_grid,
               'min_product_price': min_product_price, 'max_product_price': max_product_price}

    request.session['pagination_sort_by'] = pagination_sort_by
    request.session['pagination_show_grid'] = pagination_show_grid
    return render(request, 'ecommerce/main_search.html', context=context)
