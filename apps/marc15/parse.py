# -*- coding: utf-8 -*-
__author__ = 'voleg'
# sweet parser of Marc1.5 ITEM

def parse_item_to_dict(item):
    byTags = '\x1e' # Разделитель тэгов
    bySubtags = '\x1f' # Разделитель подтегов
    item_fields = {}
    for e in item.split(byTags):
        newTag = e[:3]
#        print(newTag)
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
#            print("\t %s - %s " % (newSubTag,newCaption))
        item_fields.update({newTag:SubtagsTempDict})
    return item_fields

def get_caption(item_dict, tag=None, subtag=None):
    return item_dict.get(tag).get(subtag)