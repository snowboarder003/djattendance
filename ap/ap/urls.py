from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import autofixture

from houses import urls as houses_urls

admin.autodiscover()
autofixture.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ap.views.home'),

	url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
    url(r'^terms/', include('terms.urls', namespace="terms")),
    url(r'^dailybread/', include('dailybread.urls', namespace="dailybread")),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

