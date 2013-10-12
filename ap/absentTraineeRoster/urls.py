from django.conf.urls import patterns, url

from absentTraineeRoster import views

urlpatterns = patterns('',
	# url(r'^attendance_form/$', views.attendance_form, name='attendance_form'),
	url(r'^attendance_form/$', views.AbsentTraineeRosterView.as_view(), name='attendance_form'),
	
)