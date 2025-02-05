import datetime

from django import template

register = template.Library()

@register.simple_tag(name="date")
def get_date():
    n = datetime.datetime.now()
    return n

@register.filter(name="Quotes")
def quotes(value):
    s = '"' + str(value) + '"'
    return s