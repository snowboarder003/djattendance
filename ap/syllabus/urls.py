from django.conf.urls import patterns, url
from syllabus.views import AboutView, SyllabusDetailView, HomeView, DetailView, TestView
from syllabus.models import Syllabus
from terms.models import Term
from terms import views

urlpatterns = patterns('',

	# url(r'^$', HomeView.as_view(), name='home-view'),

	url(r'^$', HomeView.as_view(model=Term), name='home-view'),	

	url(r'^(?P<term>(Fa|Sp)\d{2})/$', AboutView.as_view(model=Syllabus), name='classlist-view'),

	url(r'^(?P<term>(Fa|Sp)\d{2})/(?P<kode>\D+)/$', DetailView.as_view(model=Syllabus), name='detail-view'),	

	# url(r'^Term/(?P<kode>\D+)/$', DetailView.as_view(model=Syllabus), name='detail-view'),

)




