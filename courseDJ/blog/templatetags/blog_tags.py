from django import template

from blog.models import Category

register = template.Library()


@register.simple_tag
def totlat_categoryes():
    catgory_list = Category.objects.filter(published=True)
    return catgory_list