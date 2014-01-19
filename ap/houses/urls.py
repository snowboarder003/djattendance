from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<house__pk>[^/]{0,50})', 'houses.views.bunk_selector'),
)
