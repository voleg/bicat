#coding: utf-8
# Create your views here.
from django.shortcuts import render_to_response
from models import *

def issues_list(request):
    issues = Article.objects.all()
    return render_to_response("blog/index.html", locals())