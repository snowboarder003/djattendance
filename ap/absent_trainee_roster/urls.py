from django.conf.urls import patterns, url

from absent_trainee_roster import views

urlpatterns = patterns('',
	# url(r'^absent_trainee_form/$', views.AbsentTraineeFormView.as_view(), name='absent_trainee_form'),
	url(r'^absent_trainee_form/$', views.absent_trainee_form, name='absent_trainee_form'),
)