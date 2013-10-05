from django.conf.urls import patterns, url

from syllabus import views

urlpatterns = patterns('',
	url(r'^$', views.current_datetime, name='index')
	)