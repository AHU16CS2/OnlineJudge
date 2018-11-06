from django import template
register = template.Library()


@register.filter
def problem_extra(题目总数):
    return "共有"+str(题目总数)+"道该类别的题目(〃'▽'〃)"
