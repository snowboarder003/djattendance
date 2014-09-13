from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
	'',
	url(r'^$', views.AnnouncementView.as_view(), name='announcement_list'),
)
