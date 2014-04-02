from django.conf.urls import patterns, url
from django.conf import settings

from schedules import views

urlpatterns = patterns('',
    url(r'list/$', views.ScheduleListView.as_view(), name='list'),
    url(r'create/$', views.ScheduleCreateView.as_view(), name='create'),
    url(r'view/(?P<pk>\d+)/', views.ScheduleDetailView.as_view(), name='view'),
    url(r'update_event/$', views.update_event, name='update_event'),
    url(r'create_event/$', views.create_event, name='create_event'),
)