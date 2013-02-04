# coding=utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from apps.marc15.BiCat.models import Doc as bicat_doc
from apps.marc15.BiKart.models import Doc as bikar_doc
from apps.marc15.BiUML.models import Doc as biuml_doc
from django.db import models
import operator
from django.template import RequestContext

#def home(request):
#    return render_to_response('blog/index.html', locals())

# todo make a search view that extracts items from all DB's. function or class based

class PublicationsList(ListView):
    """
    Выводим список элементов базы
    """
    template_name = "Publications/List.html"
    context_object_name = 'doc_item_list'
    paginate_by = 20
    def get_queryset(self):
        # todo ordering here in queryset
        queryset = super(PublicationsList, self).get_queryset()
        return queryset.order_by('-doc_id')

#    def get_context_data(self, **kwargs):
#        super(PublicationsList, self).__init__()


class PublicationDetails(DetailView):
    """
    Формируем детальное описание объекта
    """
    template_name = "Publications/Details.html"
    context_object_name = 'doc_item'
    slug_field = 'doc_id'
    slug_url_kwarg = 'doc_id'


#    def get_context_data(self, **kwargs):
#        # Call the base implementation first to get a context
#        context = super(BiCatDocDetails, self).get_context_data(**kwargs)
#        # Add in a QuerySet of all the books
#        bicatdocs_objects = bicat_doc.objects.all()
#        context['bicat_docs_list'] = bicatdocs_objects
#        return context

@csrf_exempt
def searchview(request):
    # it's terrible i now
    bicat_docs = bicat_doc.objects.all()
    bikar_docs = bikar_doc.objects.all()
    biuml_docs = biuml_doc.objects.all()
    search_query = request.GET['search']
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
