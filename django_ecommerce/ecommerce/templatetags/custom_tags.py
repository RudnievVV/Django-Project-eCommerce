from django import template
from django.utils.html import mark_safe


register = template.Library()


@register.simple_tag
def breadcrumbs(url_path):
    breadcrumbs_html = """<div class="col-md-9">
                              <div class="bread-crumb">
                                <ul>
                                  <li><a href="#">home</a></li>"""

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

