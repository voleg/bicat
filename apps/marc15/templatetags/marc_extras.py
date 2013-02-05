# coding: utf-8
__author__ = 'voleg'
from django import template
register = template.Library()

@register.filter
def force_string(value):
    """
    template filter to check output data to
    translate list in JSON field to string
    """
    if isinstance(value, list):
        return '; '.join([e for e in value])
    return value

@register.filter
def force_list(value):
    """
    template filter to check output data to
    translate string in JSON field to list
    """
    if not isinstance(value, list):
        return [value]
    return value