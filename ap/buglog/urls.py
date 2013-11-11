from django.conf.urls import patterns, url

from buglog import views

urlpatterns = patterns('',
    url(r'thanks/$', views.BugThanksView.as_view(), name='thanks'),
    url(r'log/$', views.BuglogView.as_view(), name='log'),
    url(r'list/$', views.BuglogListView.as_view(), name='list'),
)