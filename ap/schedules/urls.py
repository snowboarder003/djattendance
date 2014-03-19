from django.conf.urls import patterns, url
from django.conf import settings

from schedules import views

urlpatterns = patterns('',
    url(r'list/$', views.ScheduleListView.as_view(), name='list'),
    url(r'create/$', views.ScheduleCreateView.as_view(), name='create'),
)
