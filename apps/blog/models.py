# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.utils.models import TimeStampedModel

class Category(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(max_length=160)
    creator = models.ForeignKey(User, related_name="creator_set")

class Article(TimeStampedModel):
    name = models.CharField('название', max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    creator = models.ForeignKey(User, blank=False, null=False, )
    issue = models.TextField('статья', max_length=20480, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('Article', (), {'slug': self.slug,})

    def __unicode__(self):
        return self.name