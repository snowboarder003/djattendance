from django.conf.urls import patterns, url
from django.conf import settings

from schedules import views

urlpatterns = patterns('',
    url(r'schedule/$', views.ScheduleDetail.as_view(), name='schedule'),
    url(r'schedule/(?P<pk>\d+)/$', views.ScheduleDetail.as_view(), name='schedule-detail'),
    url(r'schedule/list/$', views.ScheduleList.as_view(), name='schedule-list'),
    url(r'schedule/create/$', views.ScheduleCreate.as_view(), name='schedule-create'),
    url(r'event/create/$', views.EventCreate.as_view(), name='event-create'),
    url(r'event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event-detail'),
    url(r'event/(?P<pk>\d+)/update/$', views.EventUpdate.as_view(), name='event-update'),
    url(r'event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event-delete'),
)
