from django import template
register = template.Library()


@register.filter
def oj_base_extra1_filter1(新闻总数):
    return "共有"+str(新闻总数)+"篇该类别的新闻(〃'▽'〃)"
