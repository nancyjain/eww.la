from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'no_terms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'automated_summarizer.views.index', name='index'),
    url(r'^proposals/', 'automated_summarizer.views.proposals', name='proposals'),
    url(r'^about/', 'automated_summarizer.views.about', name='about'),
    url(r'^contact/', 'automated_summarizer.views.contact', name='contact'),
    url(r'^summarizer/', include('automated_summarizer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
