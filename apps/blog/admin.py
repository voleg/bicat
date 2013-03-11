from django.contrib import admin
from models import Article
from django_markdown.admin import MarkdownModelAdmin

class ArticleAdmin(MarkdownModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Article, ArticleAdmin)