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
            if breadcrumb == (len(url_path) - 2):
                breadcrumbs_html += '<li><a href="#">' + f"{url_path[breadcrumb]}</a></li>"
            else:
                breadcrumbs_html += '<li><a href="#">' + f"{url_path[breadcrumb]}</a></li><li>\</li>"
    breadcrumbs_html += """</ul>
                          </div>
                        </div>"""
    return mark_safe(breadcrumbs_html)


@register.simple_tag
def all_categories(usage_place):
    all_categories_list = Category.objects.all()
    all_categories_html = ''
    if usage_place == 'main_search':
        for category in all_categories_list:
            if category.category_products_count():
                all_categories_html += f"<option class='computer'>{category.title}</option>"
    if usage_place == 'categories_list':
        for category in all_categories_list:
            if category.category_products_count():
                all_categories_html += f"<li><a href='{category.get_absolute_url()}'>{category.title}</a></li>"

    return mark_safe(all_categories_html)


@register.filter
def add_css(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes = f'{arg}'
    return value.as_widget(attrs={'class': css_classes})
