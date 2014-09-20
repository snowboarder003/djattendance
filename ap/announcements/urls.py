from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
	'',
	url(r'^$', views.AnnouncementCreateView.as_view(), name='announcement_create'),
	url(r'^$', views.AnnouncementListView.as_view(), name='announcement_list'),
)
