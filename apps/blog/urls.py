__author__ = 'voleg'
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', IssuesListView.as_view()),
    url(r'(?P<slug>.*)$', IssueDetailView.as_view(), name='Article'),
)