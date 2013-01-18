#coding: utf-8
__author__ = 'voleg'
from django.forms.widgets import Textarea
from parse import parse_item_to_dict, get_marc_string

class MarcFormatWidget(Textarea):
    """Pritty MarcCoded Output"""
    def __init__(self, attrs=None):
        # The 'rows' and 'cols' attributes are required for HTML correctness.
        default_attrs = {'cols': '150', 'rows': 50}
        if attrs:
            default_attrs.update(attrs)
        super(MarcFormatWidget, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
#        if not isinstance(value, basestring) and value is not None:
        value = get_marc_string(parse_item_to_dict(value))
        return super(MarcFormatWidget, self).render(name, value, attrs)