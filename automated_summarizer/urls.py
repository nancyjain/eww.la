from django.conf.urls import patterns, url

from automated_summarizer import views

urlpatterns = patterns('',
    url(r'^$', views.input, name='input'),
    url(r'^result/', views.output, name='output'),
)