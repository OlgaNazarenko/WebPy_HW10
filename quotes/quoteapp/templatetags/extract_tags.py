from django import template
from django.utils.safestring import mark_safe
register = template.Library()


def transform_tags(quote_tags):
    return mark_safe(', '.join([f"<a href='/search_tag/{name}'>#{name}</a>" for name in quote_tags.all()]))


register.filter('transform_tags', transform_tags)
