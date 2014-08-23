from django.conf.urls import patterns, url
from syllabus.views import SyllabusListView, SyllabusDetailView, SyllabusDeleteView, SyllabusCreateView, SessionCreateView, SessionDeleteView, SessionDetailView, pdf_view
from syllabus.models import Syllabus, Session

urlpatterns = patterns('',

	url(r'^$', SyllabusListView.as_view(), name='syllabus-list'),	

	url(r'^(?P<pk>\d+)$', SyllabusDetailView.as_view(), name='syllabus-detail'),

	url(r'^add.html$', 
        SyllabusCreateView.as_view(), name='add-syllabus'),
 
	url(r'^delete/(?P<pk>\d+)$', 
        SyllabusDeleteView.as_view(), name='delete-syllabus'),	

    url(r'^(?P<syllabus_pk>\d+)/add$', 
        SessionCreateView.as_view(), name='add-session'),

    url(r'^(?P<syllabus_pk>\d+)/(?P<pk>\d+)/delete$', 
        SessionDeleteView.as_view(), name='delete-session'),

    url(r'^(?P<syllabus_pk>\d+)/session/(?P<pk>\d+)$', SessionDetailView.as_view(), name='session-detail'),

    url(r'^(?P<syllabus_pk>\d+)/pdf$', 
        pdf_view, name='pdf-view'),
)




