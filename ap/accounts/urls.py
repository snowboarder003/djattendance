from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views
from accounts.models import User
from accounts.views import UserDetailView, UpdateEmailView
from django.contrib.auth.views import password_change, password_change_done

urlpatterns = patterns(
    '',
    url(r'^password_change$', password_change, {'template_name': 'accounts/password_change_form.html'}, name='password-change'),
    url(r'^password_change_done$', password_change_done, {'template_name': 'accounts/password_change_done.html'}, name='password-change-done'), 
    url(r'^(?P<pk>\d+)/email_change/$', UpdateEmailView.as_view(), name='email-change'),
    url(r'^(?P<pk>\d+)/user_detail$', UserDetailView.as_view(),name='user-detail')
)
