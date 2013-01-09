# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models.query import QuerySet
from django.db import models

class ItemQuerySet(QuerySet):
    """
    Супер метод для извлечения значений из поля ITEM

    """
    def get_by_tag_and_subtag(self, tag=None, subtag=None):
#        print('you asked %s and %s ' % (tag, subtag))

        items = {}
        for i in self:
            for e in i.item.split('\x1e'):
                newTag = e[:3]
                print(newTag)
                for f in e.split('\x1f'):
                    newSubTag = f[:1]
                    newCaption = f[1:]
                    print(" %s - %s " % (newSubTag,newCaption))
        return items

class ItemManager(models.Manager):
    def get_query_set(self):
        return ItemQuerySet(self.model, using=self._db)

    def __getattr__(self, item):
        if item.startswith('_'):
            raise AttributeError(item)
        else:
            return getattr(self.get_query_set(), item)

#    def get_by_tag_and_subtag(self):
#        return self.get_query_set().get_by_tag_and_subtag()