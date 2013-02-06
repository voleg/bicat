__author__ = 'voleg'
from django.contrib import admin
from django.db import models
from models import Doc, Tag, Inv, Invoff
from apps.marc15.widgets import MarcFormatWidget

class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'item_title', 'item_author_main')
    list_display_links = ('doc_id', 'item_title', 'item_author_main')
    fieldsets = [
        ('Test', {'fields': [x.name for x in Doc._meta.fields if x.name.startswith('item_')]}),
        ('ITEM', {'fields': ('item',) }),
        ('Info', {'fields': ('doc_id', 'rectype', 'biblevel')})
    ]
    formfield_overrides = {
        models.TextField:  {'widget': MarcFormatWidget},
    }
#    list_filter = ('item_author2',)
    search_fields = ('item',)

class TagAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Tag._meta.fields])
    list_display_links = list_display

class InvAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Inv._meta.fields])
    list_display_links = list_display

class InvoffAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Invoff._meta.fields])
    list_display_links = list_display

admin.site.register(Doc, DocAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Inv, InvAdmin)
admin.site.register(Invoff, InvoffAdmin)