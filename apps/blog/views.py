# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from apps.BiCat.models import Doc as bicat_doc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def home(request):
#    return render_to_response('blog/index.html', locals())

class MyPaginator(Paginator):
    def __init__(self):
        super(MyPaginator, self).__init__()


class Home(ListView):
    context_object_name = 'bicat_docs_list'
    paginate_by = 10
    bicat_docs_list = bicat_doc.objects.all().order_by('-doc_id')
    queryset = bicat_docs_list

class BiCatDocDetails(DetailView):
    context_object_name = 'bicat_doc'
    model = bicat_doc
    slug_field = 'doc_id'
    slug_url_kwarg = 'doc_id'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BiCatDocDetails, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        bicatdocs_objects = bicat_doc.objects.all()
        context['bicat_docs_list'] = bicatdocs_objects
        return context