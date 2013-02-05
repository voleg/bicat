# coding=utf-8
from django.views.generic import ListView, DetailView

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

class PublicationDetails(DetailView):
    """
    Формируем детальное описание объекта
    """
    template_name = "Publications/Details.html"
    context_object_name = 'doc_item'
    slug_field = 'doc_id'
    slug_url_kwarg = 'doc_id'
