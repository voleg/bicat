from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(max_length=160)
    creator = models.ForeignKey(User, related_name="creator_set")
