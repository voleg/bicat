__author__ = 'voleg'
from django.conf.urls import patterns, url
from views import issues_list

urlpatterns = patterns('',
    url(r'$', issues_list, name='issue'),
)