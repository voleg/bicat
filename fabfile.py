# coding: utf-8
from fabric.contrib import django
django.settings_module('BiblCatalog.settings')
from deploy_fabric.fabfile import *
