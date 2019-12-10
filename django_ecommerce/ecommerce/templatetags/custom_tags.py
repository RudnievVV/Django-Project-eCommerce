from django import template
from django.utils.html import mark_safe
from ecommerce.models import Product, Category


register = template.Library()


@register.simple_tag
def breadcrumbs(url_path):
    breadcrumbs_html = """<div class="col-md-9">
                              <div class="bread-crumb">
                                <ul>
                                  <li><a href="/">home</a></li>"""

    url_path = url_path.split('/')
    for breadcrumb in range(len(url_path) - 1):
        if url_path[breadcrumb] == '':
            breadcrumbs_html += '<li>\</li>'
        else:
            breadcrumbs_html += '<li><a href="#">' + f"{url_path[breadcrumb]}</a></li>"
    breadcrumbs_html += """</ul>
                          </div>
                        </div>"""
    return mark_safe(breadcrumbs_html)


@register.simple_tag
def new_arrivals():
    new_arrivals_list = Product.objects.filter(available=True).order_by('-created_at')[:7]
    new_arrivals_html = ''
    for product in new_arrivals_list:
        new_arrivals_html += f"""
        <div class="item">
            <div class="product-block ">
                <div class="image"><a href="{product.get_absolute_url()}"><img class="img-responsive" title="{product.title}" alt="{product.title}" src="{product.image.url}"></a> </div>
                <div class="product-details" >
                    <div class="product-name">
                        <h3><a href="{product.get_absolute_url()}">{product.title}</a></h3>
                    </div>
                    <div class="price"><span class="price-new">{product.price}</span></div>
                    <div class="product-hov">
                        <ul>
                            <li class="wish"><a href="#"></a></li>
                            <li class="addtocart"><a href="#"> Add to Cart </a></li>
                            <li class="compare"><a href="#"></a></li>
                        </ul>
                    <div class="review"><span class="rate"><i class="fa fa-star rated"></i><i class="fa fa-star rated"></i><i class="fa fa-star rated"></i><i class="fa fa-star rated"></i><i class="fa fa-star"></i></span></div>
                    </div>
                </div>
            </div>
        </div>"""
    return mark_safe(new_arrivals_html)


@register.simple_tag
def all_categories():
    all_categories_list = Category.objects.all()
    all_categories_html = ''
    for category in all_categories_list:
        all_categories_html += f"<option class='computer'>{category.title}</option>"

    return mark_safe(all_categories_html)
