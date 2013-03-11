# coding=utf-8
__author__ = 'voleg'
from django.db import models
from datetime import datetime
from apps.utils.models import TimeStampedModel

class SearchHits(TimeStampedModel):
    query = models.CharField(u'поисковый запрос', max_length=255, blank=True, null=True)
    ip_address = models.IPAddressField(u'Адрес',blank=True, null=True)
    user_agent = models.CharField(u'Агент пользователя', max_length=255, blank=True, null=True)
    referer = models.CharField(u'ссылающийся URL', max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return ' '.join([str(self.id), self.query])

    class Meta:
        verbose_name = u'Поисковый запрос'
        verbose_name_plural = u'Поисковые запросы'
