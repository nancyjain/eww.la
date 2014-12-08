from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'no_terms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^summarizer/', include('automated_summarizer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
