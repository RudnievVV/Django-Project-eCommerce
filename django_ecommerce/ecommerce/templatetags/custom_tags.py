from django import template
from ecommerce.models import Category
from django.utils.html import mark_safe


register = template.Library()


@register.simple_tag
def category_list_with_subcategories(all_categories: list):
    """creating html code with categories and subcategories inside base.html megamenu"""
    all_categories_html = ''
    all_categories_html = _megamenu_category_list_with_subcategories(all_categories, all_categories_html)
    
    return mark_safe(all_categories_html)


def _megamenu_category_list_with_subcategories(all_categories: list, all_categories_html: str):
    """creating megamenu categories html structure"""
    for category in all_categories:
        if category.root_category:
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


def _megamenu_subcategory_subcategories(sub_category: Category):
    """creating subcategories of subcategories through recursion"""
    sub_categories_html = ''
    if sub_category.sub_categories.all():
        sub_categories_html += f'''<li class="triangle-right">
                                    <a href="{ sub_category.get_absolute_url() }">{ sub_category.title }</a>
                                    <ul class="dropdown-sub-menu">'''
        for sub_category in sub_category.sub_categories.all():
            sub_categories_html += _megamenu_subcategory_subcategories(sub_category)
        sub_categories_html += '</ul></li>'
    else:
        sub_categories_html += f'<li><a href="{ sub_category.get_absolute_url() }">{ sub_category.title }</a></li>'

    return sub_categories_html


@register.simple_tag
def product_page_thumbnail_images(product_additional_images: list):
    """creating html code with thumbnail block of product additional images"""
    thumbnail_block_html = ''
    for thumbnail_number in range(len(product_additional_images)):
        thumbnail_block_html += f'''<div class="column">
									<img class="demo cursor" src="{ product_additional_images[thumbnail_number].image.url }" onclick="currentSlide({ thumbnail_number + 2 })" alt={ product_additional_images[thumbnail_number].product.title }">
								</div>'''
        
    return mark_safe(thumbnail_block_html)
