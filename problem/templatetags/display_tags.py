from django import template
register = template.Library()


@register.filter
def display_tags(标签们, id):
    #print(标签们[id])
    return 标签们[id]





