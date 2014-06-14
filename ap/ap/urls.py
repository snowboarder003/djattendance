from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

import autocomplete_light
# import every app/autocomplete_light_registry.py
import accounts.autocomplete_light_registry
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import autofixture

from tastypie.api import Api
from leaveslip_api.resources import IndividualSlipResource, GroupSlipResource, MealOutSlipResource, NightOutSlipResource


admin.autodiscover()
autofixture.autodiscover()

urlpatterns = patterns('',
	url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
    url(r'^$', 'ap.views.home'),
    url(r'^base_example/$', 'ap.views.base_example'),

    url(r'^terms/', include('terms.urls', namespace="terms")),
    url(r'^dailybread/', include('dailybread.urls', namespace="dailybread")),
    url(r'^schedules/', include('schedules.urls', namespace="schedules")),
	url(r'^attendance/', include('attendance.urls', namespace="attendance")),
    url(r'^leaveslips/', include('leaveslips.urls', namespace="leaveslips")),

    # Examples:
    # url(r'^$', 'ap.views.home', name='home'),
    # url(r'^ap/', include('ap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # django-autocomplete-light view and staff debug view
    url(r'^autocomplete/', include('autocomplete_light.urls')),


    # leaveslips apis
    url(r'^leaveslip-api/', include(IndividualSlipResource().urls)),
    url(r'^leaveslip-api/', include(GroupSlipResource().urls)),
    url(r'^leaveslip-api/', include(MealOutSlipResource().urls)),
    url(r'^leaveslip-api/', include(NightOutSlipResource().urls)),
)

