from django.template import Library

register = Library()

@register.filter(name="odd")
def get_odd(values):
    return [x for x in values if x % 2 == 1]


@register.filter(name="app_style")
def format_to_app_style(date):
    return date.strftime('%Y/%m/%d %H')
