# coding=utf-8
from django.core.exceptions import FieldError
from django.utils.datastructures import MultiValueDictKeyError

__author__ = 'voleg'
import operator
from django.db import models
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from apps.marc15.BiCat.models import Doc as bicat_doc
from apps.marc15.BiKart.models import Doc as bikar_doc
from apps.marc15.BiUML.models import Doc as biuml_doc
from models import SearchHits


# сделано под впечатлением от django.contrib.admin.views.main
# Apply keyword searches.
def construct_search(field_name):
    if field_name.startswith('^'):
        return "%s__istartswith" % field_name[1:]
    elif field_name.startswith('='):
        return "%s__iexact" % field_name[1:]
    elif field_name.startswith('@'):
        return "%s__search" % field_name[1:]
    else:
        return "%s__icontains" % field_name

@csrf_exempt
def searchview(request, curent_base=None):
    # it's terrible i now
    bicat_docs = bicat_doc.objects.all()
    bikar_docs = bikar_doc.objects.all()
    biuml_docs = biuml_doc.objects.all()
    greeting = u'Увы ...'

    search_query = request.POST.get('q', None)

    try:
        search_query = request.GET['q']
    # except MultiValueDictKeyError:
    except:
        return redirect('/')

    ua = request.META.get('HTTP_USER_AGENT', None)
    ip = request.META.get('REMOTE_ADDR', None)
    ref = request.META.get('HTTP_REFERER', None)

    if not 'bot' in ua.lower():
        try:
            SearchHits(query=search_query, ip_address=ip, user_agent=ua, referer=ref).save()
        except:
            pass

    hint = ''
    if r'bicat' in request.path:
        search_bases = [bicat_docs]
        hint = u'Поиск по Книгам'
    elif r'bikart' in request.path:
        search_bases = [bikar_docs]
        hint = u'Поиск по Статьям'
    elif r'biuml' in request.path:
        search_bases = [biuml_docs]
        hint = u'Поиск по УМЛ'
    else:
        search_bases = [bicat_docs, bikar_docs, biuml_docs]

    search_fields = ['item']

    orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]

    if search_query == '' or len(search_query) <= 3:
        bad_alert =True

    elif search_query.startswith('"') and search_query.endswith('"'):
        search_query = search_query[1:-1].strip()
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]
        greeting = u'Точное совпадение с:'

    elif search_query.startswith('tag"') and search_query.endswith('"'):
        search_fields = ['=marc_indexed_tags__term']
        orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]
        search_query = search_query[4:-1].strip()
        greeting = u'Поиск по тегу'
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]

    elif search_query.startswith('author"') and search_query.endswith('"'):
        search_fields = ['=marc_indexed_authors__term']
        orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]
        search_query = search_query[7:-1].strip()
        greeting = u'Поиск по Автору:'
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]

    elif search_query.startswith('source"') and search_query.endswith('"'):
        search_fields = ['=marc_indexed_sourcename__term']
        orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]
        search_query = search_query[7:-1].strip()
        greeting = u'Поиск по Источнику:'
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]

    elif search_query.startswith('year"') and search_query.endswith('"'):
        search_fields = ['=marc_indexed_years__term']
        orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]
        search_query = search_query[5:-1].strip()
        greeting = u'Поиск по Году издания:'
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]

    elif search_query.startswith('pub"') and search_query.endswith('"'):
        search_fields = ['=marc_indexed_publishers__term']
        orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]
        search_query = search_query[4:-1].strip()
        greeting = u'Поиск по Издательствам:'
        queries = [models.Q(**{orm_lookup: search_query}) for orm_lookup in orm_lookups]

    else:
        for query in search_query.split():
            queries = [models.Q(**{orm_lookup: query}) for orm_lookup in orm_lookups]
            greeting = u'Полнотекстовый поиск'

    search_results = []
    for base in search_bases:
        try:
            qs = base.filter(reduce(operator.or_, queries)).order_by('-doc_id')
        except:
            qs = ''
        search_results.extend([qs])

    return render_to_response('Publications/search_results.html', {
        'search_results': search_results,
        'search_query': search_query,
        'greeting': greeting,
        'hint': hint,
        }, context_instance=RequestContext(request))


def item_change_time_view(request):
    return render_to_response('Publications/items_added_today.html')

