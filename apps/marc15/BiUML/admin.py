__author__ = 'voleg'
from django.contrib import admin
import models
from ..BiCat.admin import DocAdmin, InvAdmin, InvoffAdmin, TagAdmin, Idx100AAdmin, Idx245AAdmin, Idx653AAdmin, MetaidxAdmin

admin.site.register(models.Doc, DocAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Inv, InvAdmin)
admin.site.register(models.Invoff, InvoffAdmin)
admin.site.register(models.Idx100A, Idx100AAdmin)
admin.site.register(models.Idx245A, Idx245AAdmin)
admin.site.register(models.Idx653A, Idx653AAdmin)
admin.site.register(models.Metaidx, MetaidxAdmin)
