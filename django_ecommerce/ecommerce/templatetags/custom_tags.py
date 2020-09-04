from django import template
from django.utils.html import mark_safe


register = template.Library()


@register.simple_tag
def category_list_with_subcategories(usage_place: str, all_categories: list):
    """creating html code with categories and subcategories inside based on usage place, used in megamenu of base.html or on 'category-page' template"""
    if usage_place == 'megamenu':
        all_categories_html = _megamenu_category_list_with_subcategories(all_categories)
    if usage_place == 'category_page':
        pass
    
    return mark_safe(all_categories_html)


def _megamenu_category_list_with_subcategories(all_categories: list):
    """creating megamenu categories html structure"""
    all_categories_html = ''
    for category in all_categories:
        if category.root_category and category.products_inside():
            if category.sub_categories.all():
                all_categories_html += f'<li class="triangle-down"><a href="{ category.get_absolute_url() }">{ category.title }'
            else:
                all_categories_html += f'<li><a href="{ category.get_absolute_url() }">{ category.title }'
            if category.new:
                all_categories_html += '<span class="new">New</span>'
            all_categories_html += '</a>'
            if category.sub_categories.all():
                all_categories_html += '<ul class="sub-menu">'
                for sub_category in category.sub_categories.all():
                    all_categories_html += _megamenu_subcategory_subcategories(sub_category)
                all_categories_html += '</ul>'
    all_categories_html += '</li>'

    return all_categories_html


def _megamenu_subcategory_subcategories(sub_category: 'ecommerce.models.Category'):
    """creating subcategories of subcategories through recursion"""
    sub_categories_html = ''
    if sub_category.sub_categories.all():
        sub_categories_html += '<li class="triangle-right">'
        sub_categories_html += f'<a href="{ sub_category.get_absolute_url() }">{ sub_category.title }</a>'
        sub_categories_html += '<ul class="dropdown-sub-menu">'
        if sub_category.sub_categories.all():
            for sub_category in sub_category.sub_categories.all():
                sub_categories_html += _megamenu_subcategory_subcategories(sub_category)
        sub_categories_html += '</ul></li>'
    else:
        sub_categories_html += f'<li><a href="{ sub_category.get_absolute_url() }">{ sub_category.title }</a></li>'

    return sub_categories_html