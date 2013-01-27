# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models import SubfieldBase, CharField, TextField
from django import forms
from django.conf import settings
from django.forms.widgets import Textarea
from django.utils import simplejson
from .parse import parse_item_to_dict, items_with_tagname, get_marc_string, get_marc_field

class TagSubtagField(CharField):

    def get_internal_type(self):
        return "CharField"

    def to_python(self, value):
        if isinstance(value, basestring) or value is None:
            return value
        return unicode(value)

    def get_prep_value(self, value):
        return self.to_python(value)


class MarcFormField(forms.Field):
    # todo implement forms for Doc.Item
    pass

class MarcItemAuthorField(TextField):
    description = "Search Authors in ITEM"
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        super(MarcItemAuthorField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(MarcItemAuthorField, self).contribute_to_class(cls, name)

    def get_db_prep_value(self, value):
         pass

    def to_python(self, value):
        if not isinstance(value, basestring):
            return value
        try:
            return get_marc_field(parse_item_to_dict(value), tag='100', subtag='a') # Загружаем данные из БД через парсер
        except ValueError, e:
        # If string could not parse as JSON it's means that it's Python
            # string saved to JSONField.
            return value

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super(MarcItemAuthorField, self).formfield(**defaults)

class MarcItemField(TextField):
    description = "An ITEM parser Field"
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
#        kwargs['max_length'] = 104
        super(MarcItemField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def contribute_to_class(self, cls, name):
        super(MarcItemField, self).contribute_to_class(cls, name)

        def get_author(model):
            main_author = get_marc_field(getattr(model, self.attname), tag='100', subtag='a')
            return main_author
        setattr(cls, 'get_%s_author' % self.name, get_author)

        def get_json(model):
            return self.get_db_prep_value(getattr(model, self.attname))

        setattr(cls, 'get_%s_json' % self.name, get_json)

        def set_json(model, json):
            setattr(model, self.attname, self.to_python(json))

        setattr(cls, 'set_%s_json' % self.name, set_json)

        test_author = MarcItemAuthorField()
        setattr(cls, 'set_%s_author' % self.name, test_author)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': MarcFormField}
        defaults.update(kwargs)
        return super(MarcItemField, self).formfield(**defaults)

    # Сериализация объекта для хранения в БД
    def get_db_prep_value(self, value):
        # todo: реализовать запись данных в таблицу в Marc-формат
        pass

    # Десириализация для вывода и обработки в программе
    def to_python(self, value):
        if not isinstance(value, basestring):
            return value
        try:
            return parse_item_to_dict(value) # Загружаем данные из БД через парсер
        except ValueError, e:
        # If string could not parse as JSON it's means that it's Python
            # string saved to JSONField.
            return value

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
        value = get_marc_string(items_with_tagname(value))
        return super(MarcFormatWidget, self).render(name, value, attrs)


# from http://djangonaut.blogspot.ru/2009/02/jsonfield-django.html
class JSONField(TextField):
    __metaclass__ = SubfieldBase

    def contribute_to_class(self, cls, name):
        super(JSONField, self).contribute_to_class(cls, name)

        def get_json(model):
            return self.get_db_prep_value(getattr(model, self.attname))

        setattr(cls, 'get_%s_json' % self.name, get_json)

        def set_json(model, json):
            setattr(model, self.attname, self.to_python(json))

        setattr(cls, 'set_%s_json' % self.name, set_json)

    def formfield(self, **kwargs):
#        kwargs['widget'] = JSONWidget(attrs={'class': 'vLargeTextField'})
        kwargs['widget'] = MarcFormatWidget(attrs={'class': 'vLargeTextField'})
        return super(JSONField, self).formfield(**kwargs)

    def get_db_prep_value(self, value):
        return simplejson.dumps(value)

    def to_python(self, value):
        value = parse_item_to_dict(value)
        if not isinstance(value, basestring):
            return value
        try:
            return simplejson.loads(value, encoding=settings.DEFAULT_CHARSET)
        except ValueError, e:
        # If string could not parse as JSON it's means that it's Python
            # string saved to JSONField.
            return value


class JSONWidget(Textarea):
    """
    Prettify dumps of all non-string JSON data.
    """

    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring) and value is not None:
            value = simplejson.dumps(value, indent=4, sort_keys=True)
        return super(JSONWidget, self).render(name, value, attrs)
