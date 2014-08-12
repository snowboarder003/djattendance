# coding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from leaveslip_api.resources import IndividualSlipResource, GroupSlipResource, TraineeResource, TrainingAssistantResource, EventResource, RollResource

from rest_framework import routers

from accounts.views import *
from schedules.views import EventViewSet, ScheduleViewSet
from attendance.views import RollViewSet
from leaveslips.views import IndividualSlipViewSet, GroupSlipViewSet

from collections import namedtuple

Route = namedtuple('Route', ['url', 'mapping', 'name', 'initkwargs'])

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ap.views.home', name='home'),
    url(r'^accounts/login/$', login, name='login'),
	url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dailybread/', include('dailybread.urls', namespace="dailybread")),
    url(r'^schedules/', include('schedules.urls', namespace="schedules")),
    url(r'^attendance/', include('attendance.urls', namespace="attendance")),
    url(r'^leaveslips/', include('leaveslips.urls', namespace="leaveslips")),
    url(r'^verse_parse/', include('verse_parse.urls', namespace="verse_parse")),
    url(r'^meal_seating/', include('meal_seating.urls')),
    url(r'^absent_trainee_roster/', include('absent_trainee_roster.urls', namespace="absent_trainee_roster")),
    url(r'^syllabus/', include('syllabus.urls', namespace="syllabus")),
    url(r'^lifestudies/', include('lifestudies.urls', namespace="lifestudies")),


    url(r'^adminactions/', include('adminactions.urls')), #django-adminactions pluggable app
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

# Note delete is not supported because we don't really want to blanket delete everything (dangerous)
class BulkUpdateRouter(routers.DefaultRouter):
    routes = routers.SimpleRouter.routes
    routes[0] = Route(
        url=r'^{prefix}{trailing_slash}$',
        mapping={
            'get': 'list',
            'post': 'create',
            'put': 'bulk_update',
            'patch': 'partial_bulk_update'
        },
        name='{basename}-list',
        initkwargs={'suffix': 'List'}
    )

# Django REST Framework API urls
# router = routers.DefaultRouter()
router = BulkUpdateRouter()
router.register(r'users', UserViewSet)
router.register(r'trainees', TraineeViewSet)
router.register(r'tas', TrainingAssistantViewSet)
router.register(r'events', EventViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'rolls', RollViewSet)
router.register(r'leaveslips', IndividualSlipViewSet)
router.register(r'groupleaveslips', GroupSlipViewSet)

api_url = r'^api/'

urlpatterns += patterns('',
    url(r'^api/trainees/gender/(?P<gender>[BS])/$', TraineesByGender.as_view()),
    url(r'^api/trainees/term/(?P<term>[1234])/$', TraineesByTerm.as_view()),
    url(r'^api/trainees/team/(?P<pk>\d+)/$', TraineesByTeam.as_view()),
    url(r'^api/trainees/teamtype/(?P<type>\w+)/$', TraineesByTeamType.as_view()),
    url(r'^api/trainees/house/(?P<pk>\d+)/$', TraineesByHouse.as_view()),
    url(r'^api/trainees/locality/(?P<pk>\d+)/$', TraineesByLocality.as_view()),
    url(r'^api/trainees/hc/$', TraineesHouseCoordinators.as_view()),
    url(r'^api/', include(router.urls)),

    # tastypie apis
    url(api_url, include(EventResource().urls)),
    url(api_url, include(GroupSlipResource().urls)),
    url(api_url, include(IndividualSlipResource().urls)),
    url(api_url, include(TrainingAssistantResource().urls)),
    url(api_url, include(TraineeResource().urls)),
    url(api_url, include(RollResource().urls)),
)

urlpatterns += staticfiles_urlpatterns()
