__author__ = 'voleg'
from django.contrib import admin
import models as bicat_models
from django.db.models.base import ModelBase

tables = ('Doc', 'Tag')
for name, var in bicat_models.__dict__.items():
    if type(var) is ModelBase and name in tables:
        admin.site.register(var)