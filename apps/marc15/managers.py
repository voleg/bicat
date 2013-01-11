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
        byTags = '\x1e' # Разделитель тэгов
        bySubtags = '\x1f' # Разделитель подтегов
        items = {}
        if doc_id:
            QS = self.filter(doc_id=doc_id)
        else:
            QS = self
        for i in QS:
            for e in i.item.split(byTags):
                newTag = e[:3]
#                print(newTag)
                SubtagsTempDict = {}
                for f in e[3:].strip().split(bySubtags):
                    newSubTag = f[:1]
                    newCaption = f[1:]
                    # Далее проверяем есть ли такой подтэг в словаре если есть дописываем через запятую к уже имеющимуся
                    if newSubTag in SubtagsTempDict.keys():
                        for k, v  in SubtagsTempDict.items():
                            if k == newSubTag:
                                newCaption = v + "," + newCaption
                    SubtagsTempDict.update({newSubTag:newCaption})
#                    print("\t %s - %s " % (newSubTag,newCaption))
                items.update({newTag:SubtagsTempDict})
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