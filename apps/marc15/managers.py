# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models.query import QuerySet
from django.db import models
from parse import parse_item_to_dict, get_caption

class ItemQuerySet(QuerySet):
    """
        метод для извлечения значений из поля ITEM
    """
    def get_next(self):
        next = self.model.objects.filter(doc_id__gt=self.model.doc_id)
        if next:
            return next[0]
        return False

    def get_prev(self):
        prev = self.model.objects.filter(doc_id__lt=self.model.doc_id)
        if prev:
            return prev[0]
        return False

#    def get_item_dict(self, doc_id=None):
#        if doc_id:
#            QS = self.filter(doc_id=doc_id)
#        else:
#            QS = self
#        for i in QS:
#            fields_dict = parse_item_to_dict(i.item)
#            return fields_dict
#
#    def get_item_item(self, tag=None, subtag=None):
#        return get_caption(self.get_item_dict(), tag=tag, subtag=subtag)
#
#    def get_next_item(self):
#        raise NotImplementedError

class ItemManager(models.Manager):
    def get_query_set(self):
        return ItemQuerySet(self.model, using=self._db)

    def __getattr__(self, item):
        if item.startswith('_'):
            raise AttributeError(item)
        else:
            return getattr(self.get_query_set(), item)