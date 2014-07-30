from django.conf.urls import patterns, url
from .views import BunkListView

urlpatterns = patterns(
	'',
	url(r'^bunks$', BunkListView.as_view(), name='bunk_list'),

)
