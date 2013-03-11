from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url=''.join([settings.STATIC_URL, 'favicon.ico']))),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalog/', include('apps.marc15.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/')),
)