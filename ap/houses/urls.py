from django.conf.urls import patterns, url
from .views import HouseListView

urlpatterns = patterns(
	'',
	url(r'^$', HouseListView.as_view(), name='list'),
)
