from django.conf.urls import patterns, url

from syllabus.views import AboutView, SyllabusDetailView, HomeView
from syllabus.models import Syllabus, Session
from terms.models import Term
from terms import views

urlpatterns = patterns('',

	# TERMS
	url(r'^(?P<code>(Fa|Sp)\d{2})/$', views.TermDetailView.as_view(), name='detail'),

	url(r'^$', HomeView.as_view(), name='home-view'),

	url(r'^(?P<code>(Fa|Sp)\d{2})/1styear/$', AboutView.as_view(model=Syllabus, 
					context_object_name="list"), name='classlist-view'),
	#url(r'^detail/', SyllabusDetailView.as_view(model=Syllabus,
	#				context_object_name="detail"), name='about-view'),
		
	# (3) TO DO: Get this URL to get to syllabus/FmoC, /TG, /GK, etc.
	url(r'^(?P<code>(Fa|Sp)\d{2})/1styear/(\D+)/$', SyllabusDetailView.as_view(model=Session, context_object_name="sl"),name='detail-view'),


	
)
