from django.conf.urls import patterns, include, url
 
 
urlpatterns = patterns('',
    url(r'^$', 'badges.views.home', name='home'),
    url(r'upload/$', 'badges.views.upload', name='upload'),
)