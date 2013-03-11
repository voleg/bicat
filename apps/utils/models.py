# coding: utf-8
__author__ = 'voleg'
from django.db import models
from fields import AutoCreatedField, AutoLastModifiedField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class TimeStampedModel(models.Model):
    """ велосипед
        Общий мета класс для производства моделей с автоматически заполняемыми полями
        дата/время создания
        дата/время изменения
    """
    created = AutoCreatedField(u"Создано")
    modified = AutoLastModifiedField(u"Изменено")

    class Meta(object):
        abstract = True


class ContentTypedModel(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True, editable=False)
    object_id = models.PositiveIntegerField(blank=True, null=True, editable=False)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True