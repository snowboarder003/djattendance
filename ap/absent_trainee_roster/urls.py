from django.conf.urls import patterns, url

from absentTraineeRoster import views

urlpatterns = patterns('',
	url(r'^absent_trainee_form/$', views.AbsentTraineeFormView.as_view(), name='absent_trainee_form'),
	
)