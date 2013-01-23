__author__ = 'voleg'
from django.contrib import admin
from django.db import models
from models import Doc, Tag
from apps.marc15.widgets import MarcFormatWidget


class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'item_ISBN', 'item_author', 'item_title', 'item_series', 'item_publish', 'item_pages', 'item_cost', 'item_last_change_timestamp')
    list_display_links = ('doc_id', 'item_last_change_timestamp', 'item_author', 'item_title', 'item_pages', 'item_publish', 'item_cost', 'item_ISBN', 'item_series')
    fieldsets = [
        ('ITEM', {'fields': ('item',) }),
        ('Info', {'fields': ('doc_id', 'rectype', 'biblevel')})
    ]
    formfield_overrides = {
        models.TextField:  {'widget': MarcFormatWidget},
    }

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'subtag', 'flags', 'separator', 'caption')

admin.site.register(Doc, DocAdmin)
admin.site.register(Tag, TagAdmin)