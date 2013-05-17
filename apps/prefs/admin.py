# coding: utf-8
from django.contrib import admin
from models import Prefs


class PrefsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'key', 'value')
    list_editable = ('key', 'value')


admin.site.register(Prefs, PrefsAdmin)