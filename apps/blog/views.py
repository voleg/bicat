# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from apps.BiCat.models import Doc as bicat_doc

#def home(request):
#    return render_to_response('blog/index.html', locals())

class Home(ListView):
    context_object_name = 'bicat_docs_list'
    queryset = bicat_doc.objects.all()[:10]

class BiCatDocDetails(DetailView):
    context_object_name = "doc_id"
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