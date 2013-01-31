__author__ = 'voleg'
from django.conf.urls import patterns, include, url
from views import PublicationsList, PublicationDetails

urlpatterns = patterns('',
    url(r'^bicat/$', PublicationsList.as_view(), name='home'),
    url(r'^bicat/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view(), name='doc-path'),
    url(r'^bikart/$', PublicationsList.as_view(), name='home'),
    url(r'^bikart/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view(), name='doc-path'),

)
