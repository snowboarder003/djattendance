from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from .models import User

urlpatterns = patterns(
    '',
    url(r'^list/$', view=views.TraineesListView.as_view(), name='trainees_list'),
    url(r'^list/active$', view=views.TraineesActiveListView.as_view(), name='trainees_active_list'),
    url(r'^list/roster$', view=views.TraineesRosterListView.as_view(), name='trainees_roster_list'),
    url(r'^list/group/teamtype$', view=views.TraineesGroupTeamTypeListView.as_view(), name='trainees_group_teamtype_list'),
    url(r'^list/group/aftclass$', view=views.TraineesGroupAftClassListView.as_view(), name='trainees_group_aftclass_list'),
    url(r'^list/group/skill$',view=views.TraineesGroupSkillListView.as_view(), name='trainees_group_skill_list'),
    url(regex=r'^(?P<pk>\d+)$', view=views.UserDetailView.as_view(), name='user_detail'),
    url(regex=r'^update/(?P<pk>\d+)$', view=views.UserUpdateView.as_view(), name='user_update'),
    url(regex=r'^email/update/(?P<pk>\d+)$', view=views.EmailUpdateView.as_view(), name='email_change'),
    url(regex=r'^password/change$', view=auth_views.password_change,
        kwargs={'template_name': 'accounts/password_change_form.html',
                'current_app': 'accounts'},
        name='password_change'),
    url(regex=r'^password/change/done$', view=auth_views.password_change_done,
        kwargs={'template_name': 'accounts/password_change_done.html',
                'current_app': 'accounts'},
        name='password_change_done'),
)
