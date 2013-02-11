# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models import SubfieldBase, CharField, TextField
from django import forms
from django.conf import settings
from django.forms.widgets import Textarea, TextInput
from django.utils import simplejson
from .parse import parse_item_to_dict, items_with_tagname, get_marc_string, get_marc_field, get_caption, item_timestamp_format, get_tag_name
from django.db import models
from django.utils.encoding import force_unicode

class VirtualField(object):
    """
    Testing VirtualField originally from http://stackoverflow.com/questions/7501557/convert-property-to-django-model-field
    """
    rel = None
    def __init__(self, *args, **kwargs):
        self.tag = kwargs.pop('tag')
        self.subtag = kwargs.pop('subtag')
        super(VirtualField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        self.attname = self.name = name
        # cls._meta.add_virtual_field(self)
        get_field = cls._meta.get_field
        cls._meta.get_field = lambda name, many_to_many=True: self if name == self.name else get_field(name, many_to_many)
        models.signals.pre_init.connect(self.pre_init, sender=cls) #, weak=False)
        models.signals.post_init.connect(self.post_init, sender=cls) #, weak=False)
        setattr(cls, name, self)

    def pre_init(self, signal, sender, args, kwargs, **_kwargs):
        sender._meta._field_name_cache.append(self)

    def post_init(self, signal, sender, **kwargs):
        sender._meta._field_name_cache[:] = sender._meta._field_name_cache[:-1]

    def __get__(self, instance, instance_type=None):
        if instance is None:
            return self
        return get_marc_field(instance.item, tag=self.tag, subtag=self.subtag)

    def __set__(self, instance, value):
        if instance is None:
             raise AttributeError(u"%s must be accessed via instance" % self.related.opts.object_name)
        get_marc_field(instance.item, tag=self.tag, subtag=self.subtag)

    def to_python(self, value):
        return get_marc_field(value.item, tag='100', subtag='a')


class MarcFormField(forms.Field):
    """
    a From to edit Marc-Document
    """
    # todo implement forms for Doc.Item
    pass


class ItemField(TextField):
    """
    Represents marc-doc coded DB field in to JSON
    """
    # todo: реализовать запись данных в таблицу в Marc-формат
    description = "An Marc-Doc ITEM parser Field"
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        super(ItemField, self).__init__(*args, **kwargs)


    def get_internal_type(self):
        return 'TextField'

    def contribute_to_class(self, cls, name):
        super(ItemField, self).contribute_to_class(cls, name)

        def get_name(model, tag=None, subtag=None):
            return get_caption(getattr(model, self.name), tag=tag, subtag=subtag)
        setattr(cls, '%s_name' % self.name, get_name)

        def get_last_change_timestamp(model):
            """ извлекаем дату последней правки из Item """
            timestamp = get_caption(getattr(model, self.attname), tag='005', subtag='0')
            return item_timestamp_format(timestamp)
        setattr(cls, '%s_last_change_timestamp' % self.name, get_last_change_timestamp)

        def get_author_main(model):
            """ Основной Автор """
            return get_caption(getattr(model, self.attname), tag='100', subtag='a')
        setattr(cls, '%s_author_main' % self.name, get_author_main)

        def get_authors_other(model):
            """ Другие Авторы """
            return get_caption(getattr(model, self.attname), tag='700', subtag='a')
        setattr(cls, '%s_authors_other' % self.name, get_authors_other)

        def get_author(model):
            """
            извлекаем Авторов из Item
            """
            author = get_caption(getattr(model, self.attname), tag='100', subtag='a')
            other_authors = get_caption(getattr(model, self.attname), tag='700', subtag='a')
            if author == "" or other_authors == "": splitter = u''
            else: splitter = u', '
            return splitter.join([author, other_authors])
        setattr(cls, '%s_author' % self.name, get_author)

        def get_faculty(model):
            """ Кафедра """
            return get_caption(getattr(model, self.attname), tag='903', subtag='d')
        setattr(cls, '%s_faculty' % self.name, get_faculty)

        def get_source(model):
            """ Источник поступления"""
            return get_caption(getattr(model, self.attname), tag='901', subtag='a')
        setattr(cls, '%s_source' % self.name, get_source)

        def get_speciality(model):
            """ Специальность (направление) """
            return get_caption(getattr(model, self.attname), tag='903', subtag='a')
        setattr(cls, '%s_speciality' % self.name, get_speciality)

        def get_type_work_program(model):
            """ Вид (контрольная, лабораторная, рабочая программа) """
            return get_caption(getattr(model, self.attname), tag='903', subtag='f')
        setattr(cls, '%s_type_work_program' % self.name, get_type_work_program)

        def get_place_and_date_of_publication(model):
            """ Место и дата издания """
            return get_caption(getattr(model, self.attname), tag='773', subtag='d')
        setattr(cls, '%s_place_and_date_of_publication' % self.name, get_place_and_date_of_publication)

        def get_other_information(model):
            """ другая информация """
            return get_caption(getattr(model, self.attname), tag='773', subtag='g')
        setattr(cls, '%s_other_information' % self.name, get_other_information)

        def get_source_name(model):
            """ Название источника """
            return get_caption(getattr(model, self.attname), tag='773', subtag='t')
        setattr(cls, '%s_source_name' % self.name, get_source_name)

        def get_entrence_date(model):
            """Дата поступления документа"""
            return get_caption(getattr(model, self.attname), tag='990', subtag='f')
        setattr(cls, '%s_entrence_date' % self.name, get_entrence_date)

        def get_series(model):
            """Серия"""
            return get_caption(getattr(model, self.attname), tag='440')
        setattr(cls, '%s_series' % self.name, get_series)

        def get_ISBN(model):
            """ISBN """
            return get_caption(getattr(model, self.attname), tag='020', subtag='a')
        setattr(cls, '%s_ISBN' % self.name, get_ISBN)

        def get_cost(model):
            """Цена"""
            return get_caption(getattr(model, self.attname), tag='020', subtag='c')
        setattr(cls, '%s_cost' % self.name, get_cost)

        def get_bibliography(model):
            """Библиография !?"""
            return get_caption(getattr(model, self.attname), tag='504', subtag='a')
        setattr(cls, '%s_bibliography' % self.name, get_bibliography)

        def get_pages(model):
            """Объём издания"""
            return get_caption(getattr(model, self.attname), tag='300', subtag='a')
        setattr(cls, '%s_pages' % self.name, get_pages)

        def get_illustrations(model):
            """Илл./тип воспроизв."""
            return get_caption(getattr(model, self.attname), tag='300', subtag='b')
        setattr(cls, '%s_illustrations' % self.name, get_illustrations)

        def get_format(model):
            """Формат"""
            return get_caption(getattr(model, self.attname), tag='300', subtag='c')
        setattr(cls, '%s_format' % self.name, get_format)

        def get_cover(model):
            """ Вид переплета """
            return get_caption(getattr(model, self.attname), tag='300', subtag='d')
        setattr(cls, '%s_cover' % self.name, get_cover)

        def get_covering_matireals(model):
            """ Сопров.мат """
            return get_caption(getattr(model, self.attname), tag='300', subtag='e')
        setattr(cls, '%s_covering_matireals' % self.name, get_covering_matireals)

        def get_shelving_index(model):
            """ Полочн.индекс """
            return get_caption(getattr(model, self.attname), tag='090', subtag='a')
        setattr(cls, '%s_shelving_index' % self.name, get_shelving_index)

        def get_cat_index(model):
            """ Кат.индекс """
            return get_caption(getattr(model, self.attname), tag='090', subtag='c')
        setattr(cls, '%s_cat_index' % self.name, get_cat_index)

        def get_author_lable(model):
            """ Авторский знак """
            return get_caption(getattr(model, self.attname), tag='090', subtag='x')
        setattr(cls, '%s_author_lable' % self.name, get_author_lable)

        def get_invent_code(model):
            """ Инвентарный номер """
            return get_caption(getattr(model, self.attname), tag='090', subtag='e')
        setattr(cls, '%s_invent_code' % self.name, get_invent_code)

        def get_title(model):
            """ Заглавие - основное заглавие """
            return get_caption(getattr(model, self.attname), tag='245', subtag='a')
        setattr(cls, '%s_title' % self.name, get_title)

        def get_next_title(model):
            """ Заглавие - Продолж.заглавия """
            return get_caption(getattr(model, self.attname), tag='245', subtag='b')
        setattr(cls, '%s_next_title' % self.name, get_next_title)

        def get_responsibility(model):
            """ Заглавие - Ответственность """
            return get_caption(getattr(model, self.attname), tag='245', subtag='c')
        setattr(cls, '%s_responsibility' % self.name, get_responsibility)

        def get_title_date_of_works(model):
            """ Заглавие - Даты произведения """
            return get_caption(getattr(model, self.attname), tag='245', subtag='f')
        setattr(cls, '%s_title_date_of_works' % self.name, get_title_date_of_works)

        def get_title_media(model):
            """ Заглавие - Носитель """
            return get_caption(getattr(model, self.attname), tag='245', subtag='f')
        setattr(cls, '%s_title_media' % self.name, get_title_media)

        def get_title_part_number(model):
            """ Заглавие - Номер части """
            return get_caption(getattr(model, self.attname), tag='245', subtag='n')
        setattr(cls, '%s_title_part_number' % self.name, get_title_part_number)

        def get_title_parallel_title(model):
            """ Заглавие - Паралельное заглавие """
            return get_caption(getattr(model, self.attname), tag='245', subtag='o')
        setattr(cls, '%s_title_parallel_title' % self.name, get_title_parallel_title)

        def get_title_part_name(model):
            """ Заглавие - Название части """
            return get_caption(getattr(model, self.attname), tag='245', subtag='p')
        setattr(cls, '%s_title_part_name' % self.name, get_title_part_name)

        def get_title_version(model):
            """ Заглавие - Версия """
            return get_caption(getattr(model, self.attname), tag='245', subtag='s')
        setattr(cls, '%s_title_version' % self.name, get_title_version)

        def get_publish(model):
            """
            Информация об Издателе
            """
            return get_caption(getattr(model, self.attname), tag='260')
        setattr(cls, '%s_publish' % self.name, get_publish)

        def get_place(model):
            return get_caption(getattr(model, self.attname), tag='260', subtag='a')
        setattr(cls, '%s_place' % self.name, get_place)

        def get_publisher(model):
            return get_caption(getattr(model, self.attname), tag='260', subtag='b')
        setattr(cls, '%s_publisher' % self.name, get_publisher)

        def get_publication_year(model):
            return get_caption(getattr(model, self.attname), tag='260', subtag='c')
        setattr(cls, '%s_publication_year' % self.name, get_publication_year)

        def get_remarks(model):
            """ Примечания """
            return get_caption(getattr(model, self.attname), tag='500', subtag='a')
        setattr(cls, '%s_remarks' % self.name, get_remarks)

        def get_tags(model):
            """ Ключевые поля (Теги) """
            return get_caption(getattr(model, self.attname), tag='653', subtag='a')
        setattr(cls, '%s_tags' % self.name, get_tags)

        def get_json(model):
            return self.get_db_prep_value(getattr(model, self.attname))
        setattr(cls, 'get_%s_json' % self.name, get_json)

        def set_json(model, json):
            setattr(model, self.attname, self.to_python(json))
        setattr(cls, 'set_%s_json' % self.name, set_json)

    # Сериализация объекта для хранения в БД
    def get_db_prep_value(self, value):
        pass

    # Десириализация для вывода и обработки в программе
    def to_python(self, value):
        if not isinstance(value, basestring):
            return value
        try:
            return parse_item_to_dict(value)
        except ValueError:
            return value


class MarcItemField(CharField):
    """
    Used to query DB table field to extract some part of data.
    Deserializes and get data from marc-document field by tag an subtag
    """
    description = "An ITEM queryer Field "
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        self.marc_tag = kwargs.pop('marc_tag', '')
        self.marc_subtag = kwargs.pop('marc_subtag', '')
        self.marc_item_raw = kwargs.pop('marc_item_raw', '')
#        self.help_text = kwargs.get('help_text', '')
#        help_text = {'help_text': u"%s %s - %s" % (self.marc_tag, self.marc_subtag, get_tag_name(tag=self.marc_tag, subtag=self.marc_subtag).next())}
#        kwargs.update(help_text)
        super(MarcItemField, self).__init__(*args, **kwargs)


    def get_internal_type(self):
        return 'CharField'

    def contribute_to_class(self, cls, name):
        super(MarcItemField, self).contribute_to_class(cls, name)

    # Сериализация объекта для хранения в БД
    def get_db_prep_value(self, value):
        """Returns field's value prepared for interacting with the database
        backend.

        Used by the default implementations of ``get_db_prep_save``and
        `get_db_prep_lookup```
        """
        pass

    # Десириализация для вывода и обработки в программе
    def to_python(self, value):
        if not isinstance(value, basestring):
            return value
        try:
            return get_marc_field(value, tag=self.marc_tag, subtag=self.marc_subtag)
        except ValueError, e:
            return value


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
