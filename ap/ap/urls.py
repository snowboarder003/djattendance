# coding: utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ap.views.home', name='home'),
    url(r'^accounts/login/$', login, name='login'),
	url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^api/', include('api.urls', namespace="api")),
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

urlpatterns += staticfiles_urlpatterns()