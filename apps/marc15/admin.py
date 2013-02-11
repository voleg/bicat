# coding: utf-8
__author__ = 'voleg'
from django.contrib import admin
from models import Tags

class TagsAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Tags._meta.fields])
    list_display_links = list_display

admin.site.register(Tags, TagsAdmin)