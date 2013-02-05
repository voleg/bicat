# coding=utf-8
__author__ = 'voleg'
from django.db import models
from datetime import datetime

class SearchHits(models.Model):
    query = models.CharField('поисковый запрос', max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField('когда это произошло',default=datetime.now() , max_length=255, blank=True, null=True)

    def __unicode__(self):
        return ' '.join([self.id, self.query, self.timestamp])