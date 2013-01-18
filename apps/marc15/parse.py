# -*- coding: utf-8 -*-
__author__ = 'voleg'
"""
sweet parser of Marc1.5 ITEM

"""

def get_tag_name(tag, subtag):
    """
    тут получаем имя тега. Тег состоит из 2-х элементов tag+subtag так уж повелось исторически ...
    """
    # todo переписать метод получения тегов т.к. тут очень много запросов к БД

    from apps.BiCat.models import Tag as cononical_tags
    print("%s - %s" % (tag, subtag))
    name = cononical_tags.objects.get(tag=str(tag), subtag=str(subtag)).caption
    print(name)
    return name

def parse_item_to_dict(item):
    """
    function to convert string in MARC1.5 format to Dict
    """
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
                        newCaption = ''.join([v, ' ,', newCaption])
            SubtagsTempDict.update({newSubTag:newCaption})
#            print("\t %s - %s " % (newSubTag,newCaption))
        item_fields.update({newTag:SubtagsTempDict})
    return item_fields

def get_marc_string(dict):
    """Geterate a solid string from input dict """
    tag_subtag_item = ''
    for a,b in dict.items():
        subtag_items = ''
        subtag_items += ''.join(['\t\t%s\t%s\n' % (key, value) for key, value in b.items()])
        tag_subtag_item += ''.join(['%s\n%s' % (a, subtag_items)])
    return tag_subtag_item

def get_caption(item_dict, tag=None, subtag=None):
    """
    Here we are looking in to Dict for some values
    expecting an Item dict

    {'TAG':{'SUBTAG':'Value'}}

    """
    if tag is not None and subtag is not None:
        return item_dict.get(str(tag)).get(str(subtag))
    elif tag is not None and subtag is None:
        return item_dict.get(str(tag))
    else:
        return get_marc_string(item_dict)

def get_marc_field(item, tag=None, subtag=None):
    """
    An input we have an Item as a raw string in Marc-Format and a couple of tag and subtag
    In the output we have a Value {'TAG':{'SUBTAG':'Value'}}
    """
    if item:
        return get_caption(parse_item_to_dict(item), tag=tag, subtag=subtag)
    else:
        raise