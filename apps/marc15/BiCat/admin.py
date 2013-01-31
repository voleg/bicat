__author__ = 'voleg'
from django.contrib import admin
from django.db import models
from models import Doc, Tag
from apps.marc15.widgets import MarcFormatWidget

class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'item_title', 'item_author')
    list_display_links = ('doc_id', 'item_title', 'item_author')
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