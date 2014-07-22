from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from tastypie.api import Api
from leaveslip_api.resources import IndividualSlipResource, GroupSlipResource, TraineeResource, TrainingAssistantResource, EventResource, RollResource
import autofixture

from rest_framework import routers

from accounts.views import *
from schedules.views import EventViewSet, ScheduleViewSet
from attendance.views import RollViewSet
from leaveslips.views import IndividualSlipViewSet, GroupSlipViewSet

admin.autodiscover()
autofixture.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ap.views.home', name='home'),
    url(r'^accounts/', include ('accounts.urls')),
    url(r'^accounts/login/$', login, name='login'),
	url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^terms/', include('terms.urls', namespace="terms")),
    url(r'^dailybread/', include('dailybread.urls', namespace="dailybread")),
    url(r'^schedules/', include('schedules.urls', namespace="schedules")),
    url(r'^attendance/', include('attendance.urls', namespace="attendance")),
    url(r'^leaveslips/', include('leaveslips.urls', namespace="leaveslips")),
    url(r'^verse_parse/', include('verse_parse.urls', namespace="verse_parse")),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^meal_seating/', include('meal_seating.urls')),
    url(r'^absent_trainee_roster/', include('absent_trainee_roster.urls', namespace="absent_trainee_roster")),
    url(r'^syllabus/', include('syllabus.urls')),
    url(r'^lifestudies/', include('lifestudies.urls')),
    url(r'^select2/', include('django_select2.urls')),

    # admin urls
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^adminactions/', include('adminactions.urls')), #django-adminactions pluggable app
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# API urls
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trainees', TraineeViewSet)
router.register(r'tas', TrainingAssistantViewSet)
router.register(r'events', EventViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'rolls', RollViewSet)
router.register(r'leaveslips', IndividualSlipViewSet)
router.register(r'groupleaveslips', GroupSlipViewSet)

urlpatterns += patterns('',
    url(r'^drf/', include(router.urls)),
    url(r'^drf/trainees/gender/(?P<gender>[bs])/$', TraineesByGender.as_view()),
    url(r'^drf/trainees/term/(?P<pk>[1234])/$', TraineesByTerm.as_view()),
    url(r'^drf/trainees/team/(?P<pk>\d+)/$', TraineesByTeam.as_view()),
    url(r'^drf/trainees/house/(?P<pk>\d+)/$', TraineesByHouse.as_view()),
    url(r'^drf/trainees/locality/(?P<pk>\d+)/$', TraineesByLocality.as_view()),
    url(r'^drf/trainees/hc/$', HouseCoordinators.as_view()),

    # tastypie leaveslips apis
    url(r'^api/', include(EventResource().urls)),
    url(r'^api/', include(GroupSlipResource().urls)),
    url(r'^api/', include(IndividualSlipResource().urls)),
    url(r'^api/', include(TrainingAssistantResource().urls)),
    url(r'^api/', include(TraineeResource().urls)),
    url(r'^api/', include(RollResource().urls)),
)
