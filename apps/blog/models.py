from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(max_length=160)
    creator = models.ForeignKey(User, related_name="creator_set")

class Article(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    creator = models.ForeignKey(User, blank=False, null=False)
    issue = models.TextField(max_length=20480, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now())

    @models.permalink
    def get_absolute_url(self):
        return 'issue', [self.slug]

    def __unicode__(self):
        return self.name