from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done

from . import views

urlpatterns = patterns(
    '',
    url(regex=r'^(?P<pk>\d+)$', view=views.UserDetailView.as_view(), name='user_detail'),
    url(regex=r'^update/(?P<pk>\d+)$', view=views.UserUpdateView.as_view(), name='user_update'),
    url(regex=r'^update/email/(?P<pk>\d+)$', view=view.sEmailUpdateView.as_view(), name='email_change'),
    url(regex=r'^update/password$', view=password_change,
        {'template_name': 'accounts/password_change_form.html'},
        name='password_change'),
    url(regex=r'^update/password/success$', view=password_change_done,
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),
)
