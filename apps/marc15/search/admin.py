# coding: utf-8
__author__ = 'voleg'
from django.contrib import admin
from models import SearchHits


class SearchHitsAdmin(admin.ModelAdmin):
    list_display = ('query', 'ip_address', 'user_agent', 'referer', 'created') #, 'modified')
    search_fields = ('query', 'ip_address', 'user_agent', 'referer', 'created')

admin.site.register(SearchHits, SearchHitsAdmin)