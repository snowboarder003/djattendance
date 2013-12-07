from django.conf.urls import patterns, url

from syllabus.views import AboutView, SyllabusDetailView, HomeView
from syllabus.models import Syllabus, Session
from terms.models import Term
from terms import views

urlpatterns = patterns('',

	# TERMS (Fa13, Sp12, etc)
	#url(r'^$', views.TermDetailView.as_view(), name='detail'),

	url(r'^$', HomeView.as_view(), name='home-view'),

	# This is BROKE right now... it doesnt like the <code>() {} thing.
	url(r'^1styear/$', AboutView.as_view(model=Syllabus, 
					context_object_name="list"), name='classlist-view'),
		
	# Need to get access to SYLLABUS model along with SESSION model.
	url(r'^1styear/(\D+)/$', 
		SyllabusDetailView.as_view(model=Syllabus, context_object_name="syl_list"), 
		name='detail-view'),	
)
