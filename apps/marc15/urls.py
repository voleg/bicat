__author__ = 'voleg'
from django.conf.urls import patterns, include, url
from views import PublicationsList, PublicationDetails
from apps.marc15.BiCat.models import Doc as bicat_doc
from apps.marc15.BiKart.models import Doc as bikar_doc
from apps.marc15.BiUML.models import Doc as biuml_doc
from views import searchview

urlpatterns = patterns('',
    url(r'bicat/$', PublicationsList.as_view(model=bicat_doc)),
    url(r'bicat/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view(model=bicat_doc), name='BiCat_doc-path'),

    url(r'bikart/$', PublicationsList.as_view(model=bikar_doc)),
    url(r'bikart/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view(model=bikar_doc), name='BiKart_doc-path'),

    url(r'biuml/$', PublicationsList.as_view(model=biuml_doc)),
    url(r'biuml/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view(model=biuml_doc), name='BiUML_doc-path'),

    url(r'search/$', searchview, name='search')
)
