# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.db.models.query import QuerySet
from django.db import models
from parse import parse_item_to_dict, get_caption

class ItemQuerySet(QuerySet):
    """
    метод для извлечения значений из поля ITEM
    """
    def get_item_dict(self, doc_id=None):
        if doc_id:
            QS = self.filter(doc_id=doc_id)
        else:
            QS = self
        for i in QS:
            fields_dict = parse_item_to_dict(i.item)
            # i like to view how it going
#            print("{0}".format("."*200))
#            for a,b in fields_dict.items():
#                print(u"{0}".format(a))
#                for c,d in b.items():
#                    print(u"\t{0} - {1}".format(c,d))
            return fields_dict

    def get_item_item(self, tag=None, subtag=None):
        return get_caption(self.get_item_dict(), tag=tag, subtag=subtag)

class ItemManager(models.Manager):
    def get_query_set(self):
        return ItemQuerySet(self.model, using=self._db)

    def get_item_changetimestamp(self):
        return self.item_changetimestamp()

    def __getattr__(self, item):
        if item.startswith('_'):
            raise AttributeError(item)
        else:
            return getattr(self.get_query_set(), item)