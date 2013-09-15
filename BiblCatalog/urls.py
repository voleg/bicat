from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url=''.join([settings.STATIC_URL, 'favicon.ico']))),
    url('^markdown/', include('django_markdown.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('apps.marc15.urls', 'catalog')),
    url(r'^blog/', include('apps.blog.urls', 'blog')),
    url(r'^$', RedirectView.as_view(url='/blog/')),
)
