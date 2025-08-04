from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.filter
def display_length(value):
    if value is None or len(value) == 0:
        return mark_safe("<p></p>")
    elif len(value) == 1:
        return mark_safe("<p>%s result</p>" % len(value))
    else:
        return mark_safe("<p>%s results</p>" % len(value))


@register.filter
def firstCap(value):
    if value:
        return value.title()
    return value
    # str = ''
    # arr = value.split(" ")
    # for w in arr:
    #     str + w.capitalize() + ""
    # return str


# register.filter("firstCap", firstCap)
