from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'houses.views.import_bunks'),
)
