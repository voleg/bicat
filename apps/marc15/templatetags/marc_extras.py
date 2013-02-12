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
    namepattern2 = r'^(?P<family>.+)[\s]+(?P<name>.[.])$'
    namere = re.compile(namepattern)
    namere2 = re.compile(namepattern2)

    if namere.match(value):
        n = namere.match(value).groupdict()
        return '%s%s %s' % (n.get('name'), n.get('father'), n.get('family'))
    elif namere2.match(value):
        n = namere2.match(value).groupdict()
        return '%s %s' % (n.get('name'), n.get('family'))