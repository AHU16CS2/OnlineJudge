from django import template
register = template.Library()


@register.filter
def div_with_percent(value, div):
    return  round( (value / div) * 100 , 3 )
