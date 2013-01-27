from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^bicat/(?P<doc_id>[-\w]+)$', BiCatDocDetails.as_view(), name='doc-path'),

)