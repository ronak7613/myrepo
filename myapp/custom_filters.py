# # custom_filters.py

# from django import template

# register = template.Library()

# @register.filter()
# def custom_range(value):
#     return range(value)

from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)