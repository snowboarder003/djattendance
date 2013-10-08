from django.conf.urls import patterns, url

from absent_trainee_roster import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^attendance_form/$', views.attendance_form, name='attendance_form'),
	url(r'^search/$', views.search),
	
)