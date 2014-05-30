from django.conf.urls import patterns, url
from django.conf import settings

from attendance import views

urlpatterns = patterns('',
    url(r'personal/$', views.AttendancePersonal.as_view(), name='attendance-personal'),
#    url(r'attendance/submit/(?P<pk>\d+)/$', views.AttendanceSubmit.as_view(), name='attendance-submit'),
)
