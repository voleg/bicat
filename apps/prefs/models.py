# coding: utf-8
from django.db import models


class Prefs(models.Model):
    name = models.CharField(u'Имя', max_length=255, blank=True, null=True)
    key = models.CharField(u'ключ', max_length=255, blank=True, null=True)
    value = models.CharField(u'значение', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'Настройка'
        verbose_name_plural = u'Настройки'

    def __unicode__(self):
        return self.name