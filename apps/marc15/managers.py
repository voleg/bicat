# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models.query import QuerySet
from django.db import models

class ItemQuerySet(QuerySet):
    """
    Супер метод для извлечения значений из поля ITEM

    """
    def get_by_tag_and_subtag(self, doc_id=None, tag=None, subtag=None):
#        print('you asked %s and %s ' % (tag, subtag))
        byTags = '\x1e'
        bySubtags = '\x1f'
        items = {}
        for i in self.filter(doc_id=doc_id):
            for e in i.item.split(byTags):
                newTag = e[:3]
                print(newTag)

                for f in e[3:].strip().split(bySubtags):
                    newSubTag = f[:1]
                    newCaption = f[1:]
                    print("\t %s - %s " % (newSubTag,newCaption))
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