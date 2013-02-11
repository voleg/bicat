__author__ = 'voleg'
from django.contrib import admin
from django.db import models
from models import Doc, Inv, Invoff, Tag, Idx100A, Idx245A, Idx653A, Metaidx
from apps.marc15.widgets import MarcFormatWidget


class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_id', 'item_title', 'item_author_main')
    list_display_links = list_display
    fieldsets = [
        # ('Test', {'fields': [x.name for x in Doc._meta.fields if x.name.startswith('item_')]}),
        ('Info', {'fields': ('doc_id', 'rectype', 'biblevel')}),
        ('ITEM', {'fields': ('item',)}),
        ('dictionaries', {'fields': ('marc_indexed_authors', 'marc_indexed_tags', 'marc_indexed_titles')}),
        ('Inventory', {'fields': ('inventory_number', 'inventory_offs')})
    ]
    formfield_overrides = {
        models.TextField:  {'widget': MarcFormatWidget},
    }
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


class Idx100AAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Idx100A._meta.fields])
    list_display_links = list_display


class Idx245AAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Idx245A._meta.fields])
    list_display_links = list_display


class Idx653AAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Idx653A._meta.fields])
    list_display_links = list_display


class MetaidxAdmin(admin.ModelAdmin):
    list_display = ([i.name for i in Metaidx._meta.fields])
    list_display_links = list_display


admin.site.register(Doc, DocAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Inv, InvAdmin)
admin.site.register(Invoff, InvoffAdmin)
admin.site.register(Idx100A, Idx100AAdmin)
admin.site.register(Idx245A, Idx245AAdmin)
admin.site.register(Idx653A, Idx653AAdmin)
admin.site.register(Metaidx, MetaidxAdmin)
