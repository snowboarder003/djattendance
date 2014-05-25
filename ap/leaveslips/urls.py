from django.conf.urls import patterns, url

from leaveslips import views

urlpatterns = patterns('',
    url(r'create/individual/$', views.IndividualSlipCreate.as_view(), name='individual-create'),
    url(r'individual/(?P<pk>\d+)$', views.IndividualSlipDetail.as_view(), name='individual-detail'),
    url(r'update/individual/(?P<pk>\d+)$', views.IndividualSlipUpdate.as_view(), name='individual-update'),

    url(r'create/group/$', views.GroupSlipCreate.as_view(), name='group-create'),
    url(r'group/(?P<pk>\d+)$', views.GroupSlipDetail.as_view(), name='group-detail'),

)

#     url(r'schedule/list/$', views.ScheduleList.as_view(), name='schedule-list'),
