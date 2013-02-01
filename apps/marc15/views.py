# coding=utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def home(request):
#    return render_to_response('blog/index.html', locals())

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
