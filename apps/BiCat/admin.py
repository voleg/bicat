__author__ = 'voleg'
from django.contrib import admin
import models as bicat_models
from django.db.models.base import ModelBase

for name, var in bicat_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)