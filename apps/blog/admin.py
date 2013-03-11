from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Article, ArticleAdmin)