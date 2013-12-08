from django.conf.urls import patterns, include, url
 
 
urlpatterns = patterns('',
    url(r'upload/$', 'urls.views.upload', name='upload'),
)