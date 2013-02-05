# coding=utf-8
__author__ = 'voleg'
import operator
from django.db import models
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from apps.marc15.BiCat.models import Doc as bicat_doc
from apps.marc15.BiKart.models import Doc as bikar_doc
from apps.marc15.BiUML.models import Doc as biuml_doc

# todo make a search view that extracts items from all DB's. function or class based

@csrf_exempt
def searchview(request):
    # it's terrible i now
    bicat_docs = bicat_doc.objects.all()
    bikar_docs = bikar_doc.objects.all()
    biuml_docs = biuml_doc.objects.all()
    try:
        search_query = request.POST['q']
    except:
        search_query = request.GET['q']
    search_fields = ['item']

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

    orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]

    if search_query.startswith('"') and search_query.endswith('"'):
        queries = [models.Q(**{orm_lookup: search_query[1:-1]}) for orm_lookup in orm_lookups]
    else:
        for query in search_query.split():
            queries = [models.Q(**{orm_lookup: query}) for orm_lookup in orm_lookups]

    bicat_qs = bicat_docs.filter(reduce(operator.or_, queries))
    bikart_qs = bikar_docs.filter(reduce(operator.or_, queries))
    biuml_qs = biuml_docs.filter(reduce(operator.or_, queries))

    search_results = [bicat_qs, bikart_qs, biuml_qs]

    return render_to_response('Publications/search_results.html', {'search_results': search_results}, context_instance=RequestContext(request))
