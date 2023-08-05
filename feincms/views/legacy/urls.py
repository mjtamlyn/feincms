from django.conf.urls import patterns, url

from feincms.views.legacy.views import handler

urlpatterns = patterns('',
    url(r'^$', handler, name='feincms_home'),
    url(r'^(.*)/$', handler, name='feincms_handler'),
)
