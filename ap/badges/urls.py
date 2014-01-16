from django.conf.urls import patterns, include, url

from badges.views import TermView
 
urlpatterns = patterns('',
    url(r'^$', 'badges.views.index', name='index'),
    # view/edit single badge
    #url(r'^view/(?P<pk>\d+)/$', 'badges.views.view', name='view_badge'),
    #url(r'^edit/(?P<pk>\d+)/$', 'badges.views.edit', name='edit_badge'),
    # view multiple badges
    url(r'^view/(?P<term>(Fa|Sp)\d{2})/$', TermView.as_view(), name='term_badges'),
    #url(r'^edit/staff/$', 'badges.views.staff', name='staff_badges'),
    # badge creation
    #url(r'^create/$', 'badges.views.create_index', name='create_index'),
    #url(r'^create/trainee/$', 'badges.views.create_trainee', name='create_trainee'),
    #url(r'^create/staff/$', 'badges.views.create_staff', name='create_staff'),
    url(r'^create/batch/$', 'badges.views.batch', name='batch'),
)