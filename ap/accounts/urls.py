from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done
from accounts import views

from accounts.models import User
from accounts.views import UserDetailView, UserUpdateView, EmailUpdateView

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)$', UserDetailView.as_view(), name='user-detail'),
    url(r'^update/(?P<pk>\d+)$', UserUpdateView.as_view(), name='user-update'),
    url(r'^update/email/(?P<pk>\d+)$', EmailUpdateView.as_view(),
        name='email-change'),
    url(r'^update/password$', password_change,
        {'template_name': 'accounts/password_change_form.html'},
        name='password-change'),
    url(r'^update/password/success$', password_change_done,
        {'template_name': 'accounts/password_change_done.html'},
        name='password-change-done'),
)
