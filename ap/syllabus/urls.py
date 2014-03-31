from django.conf.urls import patterns, url
from syllabus.views import CLView, SyllabusDetailView, HomeView, DetailView, TestView, DeleteSyllabusView, AddSyllabusView
from syllabus.models import Syllabus
from terms.models import Term
from terms import views


urlpatterns = patterns('',

	# url(r'^$', HomeView.as_view(), name='home-view'),

	url(r'^$', HomeView.as_view(model=Term), name='home-view'),	

	url(r'^(?P<term>(Fa|Sp)\d{2})/$', CLView.as_view(model=Syllabus,
			context_object_name="list"), name='classlist-view'),

	url(r'^(?P<term>(Fa|Sp)\d{2})/(?P<kode>\D{0,5})/$', DetailView.as_view(model=Syllabus), name='detail-view'),

	url(r'^add_syllabus.html$', AddSyllabusView.as_view(), name='add-syllabus'),

	url(r'^(?P<term>(Fa|Sp)\d{2})/delete/(?P<pk>\d+)$', DeleteSyllabusView.as_view(), name='delete-syllabus'),	

	# url(r'^Term/(?P<kode>\D+)/$', DetailView.as_view(model=Syllabus), name='detail-view'),

)




