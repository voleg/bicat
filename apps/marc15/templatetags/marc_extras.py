# coding: utf-8
__author__ = 'voleg'
from django import template
import re
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
#        if ',' in value: return value.split(',')
#        if ';' in value: return value.split(';')
        return [value]
    return value

@register.filter
def place_initials_first(value):
    """
    template filter to reformat names
    Smith J.S. -> J.S. Smith
    """
    namepattern = r'^(?P<family>.+)[\s]+(?P<name>.[.])[\s]*(?P<father>.[.])$'
    namere = re.compile(namepattern)

    if namere.match(value):
        n = namere.match(value).groupdict()

        value = '%s%s %s' % (n.get('name'), n.get('father'), n.get('family'))

    return value