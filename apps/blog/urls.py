from django.conf.urls import patterns, include, url
from views import PublicationsList, PublicationDetails

urlpatterns = patterns('',
    url(r'^bicat/$', PublicationsList.as_view()),
    url(r'^bicat/(?P<doc_id>[-\w]+)$', PublicationDetails.as_view()),
)