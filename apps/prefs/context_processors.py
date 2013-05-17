# coding: utf-8
from models import Prefs

def context_prefs(request):

    prefs = {}
    for p in Prefs.objects.all():
        prefs.update({p.key:p.value})

    return prefs
