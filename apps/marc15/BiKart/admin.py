__author__ = 'voleg'
from django.contrib import admin
import models
from ..BiCat.admin import DocAdmin, TagAdmin

admin.site.register(models.Doc, DocAdmin)
admin.site.register(models.Tag, TagAdmin)