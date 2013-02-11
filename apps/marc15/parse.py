# -*- coding: utf-8 -*-
__author__ = 'voleg'
from django.conf import settings
#
# sweet parser of Marc1.5 ITEM Field
#
# todo: refactor that bunch of stupid functions

def get_tag_name(tag, subtag):
    """
    тут получаем имя тега. Тег состоит из 2-х элементов tag+subtag так уж повелось исторически ...
    """
    # todo: rewrite a function to make it more light and fast. The TAG field in model really does not changes in time it kind a like some key-value storage, so it may be a reason to represent data in a table like a static dict in a code if it would be a bottleneck place. Keep it in mind

    from models import Tags as cononical_tags # We take Tags from b_cat DB as a cononical
    try:
        name = cononical_tags.objects.get(tag=str(tag), subtag=str(subtag)).caption
    except:
        name = u"<неизвестный тег>"
    yield name

def parse_item_to_dict(item):
    """
    function to convert string in MARC1.5 format to JSON
    {
       "Tag": {
           "subtag": "value",
           "subtag": "value",
           "subtag": [ "value_1",
                       "value_2" ]
       }
       ...
    }
    """
    byTags = '\x1e'
    bySubtags = '\x1f'
    item_fields = {}
    for e in item.split(byTags):
        newTag = e[:3]
        SubtagsTempDict = {}
        for f in e[3:].strip().split(bySubtags):
            newSubTag = f[:1]
            newCaption = f[1:]

            # Splitting strings
            if not isinstance(newCaption, (list, dict)):
                if ';' in newCaption:
                    newCaption = newCaption.split(';')
                if newTag not in settings.DO_NOT_SPLIT_TAGS and ',' in newCaption:
                    newCaption = newCaption.split(',')
    #                elif newTag == '653' and ',' in newCaption:
#                    # Проверяем если тег = 653 (ключевые поля) и он содержит строку с запятыми то делим их
#                    newCaption = newCaption.split(',')
            # Далее проверяем есть ли такой подтэг в словаре, если есть делаем список
            if newSubTag in SubtagsTempDict.keys():
                for k, v in SubtagsTempDict.items():
                    if k == newSubTag:
                        if type(v) is not list:
                            v = [v]
                        if type(newCaption) is not list:
                            newCaption = [newCaption]
                        newCaption = v + newCaption
            SubtagsTempDict.update({newSubTag:newCaption})
        item_fields.update({newTag:SubtagsTempDict})
    return item_fields

def items_with_tagname(item):
    """
    работает с  марк-документом (сырой строкой, json представлением)
    Добавим имя к Тегам
    {TAG:{SUBTAG:VALUE}} -> {TAG:{"SUBTAG Name":VALUE}}
    """
    dict = {}
    if not isinstance(item, {}.__class__): item = parse_item_to_dict(item)
    for tag, subtag_value in item.items():
        name_value={}
        for subtag, value in subtag_value.items():
            name = get_tag_name(tag,subtag).next()
            name = '\t'.join([subtag, name])
            name_value.update({name:value})
        dict.update({tag:name_value})
    return dict


def get_marc_string(dict):
    """Geterate a sorted, solid string from input dict """
    tag_subtag_item = ''
    for key in sorted(dict.iterkeys()):
        subitem = dict.get(key)
        subtag_items = ''
        for subkey in sorted(subitem.iterkeys()):
            newsubitem = subitem.get(subkey)
            if type(newsubitem) is not list:
                subtag_items += ''.join([u'\t%s:\n\t\t%s\n' % (subkey, newsubitem)])
            else:
                subtag_items = ''.join([u'\t%s:\n' % subkey])
                subtag_items += ''.join([u'\t\t%s\n' % e for e in newsubitem])

        tag_subtag_item += ''.join([u'%s\n%s' % (key, subtag_items)])

    return tag_subtag_item

def get_caption(item_dict, tag=None, subtag=None):
    """
    Here we are looking in to Dict for some values
    expecting an Item_dict is a dict

    {'TAG':{'SUBTAG':'VALUE'}}
    Also it checks VALUE to force dict in there to become a string divided by commas

    Если указан только тег то проходимся пр всем подтегам и их значениям, объединяя их через запятую
    """
    if tag is not None and subtag is not None:
        try:
            return item_dict.get(tag).get(subtag)
        except(AttributeError):
            return u""
    elif tag is not None and subtag is None:
        try:
            items_in_all_subtags_of_tag = item_dict.get(tag)
            if isinstance(items_in_all_subtags_of_tag, dict):
                string_of_items = ''
                splitter = ''
                items_counter = 0
                for subtag, items_under_subtag in items_in_all_subtags_of_tag.items():
                    if isinstance(items_under_subtag, list):
                        string_of_items += ', '.join(items_under_subtag)
                    else:
                        if items_counter > 0:
                            splitter = ', '
                        string_of_items += ''.join([splitter, items_under_subtag])
                    items_counter += 1
                return string_of_items
        except(AttributeError):
            return u""
    else:
        return get_marc_string(item_dict)


def get_marc_field(item, tag=None, subtag=None):
    """
    On input we have an Item as a raw string in Marc-Format and a couple of tag and subtag
    In the output we have a Value {'TAG':{'SUBTAG':'Value'}}
    """
    if item:
        return get_caption(parse_item_to_dict(item), tag=tag, subtag=subtag)
    else:
        raise


def item_timestamp_format(timestamp):
    """Преобразуем строку ГодМесяцДеньЧасМинутаСекундаМилисекунда В нечто более человеко читаемое"""
    year, month, day, hour, minute, seconds = timestamp[:4], timestamp[4:6], timestamp[6:8],\
                                              timestamp[8:10], timestamp[10:12], timestamp[12:14]
    return " ".join([".".join([year, month, day]), ":".join([hour, minute, seconds])])


#def ReversedDic(func):
#    """
#    декоратор инвертирующий порядок элементов в списке??? или словаре ?
#    """
#
#    def the_wrapper(arg):
#        input_dict = func(arg)
#        return reversed(input_dict.items())
#
#    return the_wrapper

def ListToStr(func):
    """
    декоратор
    проверяем вывод функции, если там список то делаем из неё строку
    """
    def the_wrapper(arg):
        input_str = func(arg)
        if isinstance(input_str, list):
            return '; '.join([e for e in input_str])
        return input_str
    return the_wrapper