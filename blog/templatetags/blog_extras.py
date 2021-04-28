from django import template

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__
