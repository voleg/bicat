__author__ = 'voleg'
from django.conf.urls import patterns, url
from views import issues_list, issue

urlpatterns = patterns('',
    url(r'$', issues_list, name='issue'),
    url(r'blog/(?P<issue_slug>[-\w]+)$', issue, name='article')
)