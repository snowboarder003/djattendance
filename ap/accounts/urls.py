from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views

##urlpatterns = patterns('',
##    url(r'^$', views.index, name='index')
##)

urlpatterns = patterns('',
    url(r'^password_change$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/password_change_form.html'}),
    url(r'^password_change_done$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/password_change_done.html'}),
)