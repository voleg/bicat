# -*- coding: utf-8 -*-
__author__ = 'voleg'
#
# sweet parser of Marc1.5 ITEM Field
#

def get_tag_name(tag, subtag):
    """
    тут получаем имя тега. Тег состоит из 2-х элементов tag+subtag так уж повелось исторически ...
    """
    # todo rewrite a function in more light and fast direction. The TAG field in model really does not changes in time it kind a like some key-value storage, so it may be a reason to represent data in a table like a static dict in a code if it would be a bottle-nec place. Keep it in mind

    from apps.BiCat.models import Tag as cononical_tags
    try:
        name = cononical_tags.objects.get(tag=str(tag), subtag=str(subtag)).caption
    except:
        name = u"<Имя тега не найдено>"
    yield name

def parse_item_to_dict(item):
    """
    function to convert string in MARC1.5 format to Dict
    """
    # todo rebuild method to produce JSON
    """
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
            # Далее проверяем есть ли такой подтэг в словаре если есть дописываем через точку-запятую к уже имеющимуся
            if newSubTag in SubtagsTempDict.keys():
                for k, v  in SubtagsTempDict.items():
                    if k == newSubTag:
                        newCaption = ';'.join([v, newCaption])
            SubtagsTempDict.update({newSubTag:newCaption})
#            print("\t %s - %s " % (newSubTag,newCaption))
        item_fields.update({newTag:SubtagsTempDict})
    return item_fields

def items_with_tagname(item):
    """
    Добавим имя к Тегам
    {TAG:{SUBTAG:VALUE}} -> {TAG:{"SUBTAG Name":VALUE}}
    """
    dict = {}
    for tag, subtag_value in parse_item_to_dict(item).items():
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
    for a in sorted(dict.iterkeys()):
        b = dict.get(a)
        subtag_items = ''
        subtag_items += ''.join(['\t%s:\n\t\t%s\n' % (key, b.get(key)) for key in sorted(b.iterkeys())])
        tag_subtag_item += ''.join(['%s\n%s' % (a, subtag_items)])
    return tag_subtag_item

def get_caption(item_dict, tag=None, subtag=None):
    """
    Here we are looking in to Dict for some values
    expecting an Item_dict is a dict

    {'TAG':{'SUBTAG':'VALUE'}}
    Also it checks VALUE to force dict in there to become a string divided by commas
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
                items_in_all_subtags_of_tag = ', '.join([values for key,values in items_in_all_subtags_of_tag.items()])
            return items_in_all_subtags_of_tag
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
    return " ".join(["-".join([year, month, day]), ":".join([hour, minute, seconds])])