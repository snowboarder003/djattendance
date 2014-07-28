from django.conf.urls import patterns, url
from .views import HouseListView, BunkListView

urlpatterns = patterns(
	'',
	url(r'^$', HouseListView.as_view(), name='house_list'),
	url(r'^bunk$', BunkListView.as_view(), name='bunk_list'),

)
