#coding: utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from models import *


class IssuesListView(ListView):
    template_name = "blog/index.html"
    model = Article
    context_object_name = 'issues'

class IssueDetailView(DetailView):
    template_name = "blog/issue.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    model = Article
    context_object_name = 'issue'


def issues_list(request):
    issues = Article.objects.all()
    return render_to_response("blog/index.html", locals())


def issue(request, slug):
    print(slug)
    return render_to_response("blog/issue.html", locals())