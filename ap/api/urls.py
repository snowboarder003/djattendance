# api urls.py
from collections import namedtuple
from django.conf.urls import patterns, include, url
from rest_framework import routers

from accounts.views import *
from schedules.views import EventViewSet, ScheduleViewSet
from attendance.views import RollViewSet
from leaveslips.views import IndividualSlipViewSet, GroupSlipViewSet

Route = namedtuple('Route', ['url', 'mapping', 'name', 'initkwargs'])

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

urlpatterns = patterns('',
    url(r'trainees/gender/(?P<gender>[BS])/$', TraineesByGender.as_view()),
    url(r'trainees/term/(?P<term>[1234])/$', TraineesByTerm.as_view()),
    url(r'trainees/team/(?P<pk>\d+)/$', TraineesByTeam.as_view()),
    url(r'trainees/teamtype/(?P<type>\w+)/$', TraineesByTeamType.as_view()),
    url(r'trainees/house/(?P<pk>\d+)/$', TraineesByHouse.as_view()),
    url(r'trainees/locality/(?P<pk>\d+)/$', TraineesByLocality.as_view()),
    url(r'trainees/hc/$', TraineesHouseCoordinators.as_view()),
    url(r'^', include(router.urls)),
)