from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
	'',
	url(r'^bunks$', views.BunkListView.as_view(), name='bunk_list'),
	url(r'^bunks/(?P<pk>\d+)$', views.BunkFormView.as_view(), name='bunk_update'),
)
