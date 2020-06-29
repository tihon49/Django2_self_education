from django import template

from blog.models import Category

register = template.Library()



def get_categoryes(context, order, count):
    """Получаем список категорий"""
    categoryes = Category.objects.filter(published=True).order_by(order)

    if categoryes is not None:
        categoryes = categoryes[:count]

    return categoryes



@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(context, order='-name', count=None, template='base/blog/categoryes.html'):
    """Template tag вывода категорий"""
    categoryes = get_categoryes(context, order,count)
    return {'template': template, 'category_list': categoryes}



@register.simple_tag(takes_context=True)
def for_category_list(context, count=None, order='-name'):
    """Template tag вывода категорий без шаблона"""
    return get_categoryes(context, order, count)