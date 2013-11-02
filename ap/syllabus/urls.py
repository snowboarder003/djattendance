from django.conf.urls import patterns, url

from syllabus.views import AboutView, SyllabusDetailView, HomeView
from syllabus.models import Syllabus

urlpatterns = patterns('',
	url(r'^about/', AboutView.as_view(model=Syllabus, 
					context_object_name="syllabus_list"), name='about-view'),
	#url(r'^detail/', SyllabusDetailView.as_view(model=Syllabus,
	#				context_object_name="detail"), name='about-view'),
	
	#url(r'^(?P<classSyllabus.code>)/$', SyllabusDetailView.as_view(), name='detail'),
	
	# (3) TO DO: Get this URL to get to syllabus/FmoC, /TG, /GK, etc.
	url(r'(?P<pk>\d+)/$', SyllabusDetailView.as_view(),
		name='detail-view'),

	url(r'^home/', HomeView.as_view(), name='home-view'),
)
