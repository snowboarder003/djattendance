from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # url(r'^$', views.___, name='home'),
    url(r'^template/create$', views.TemplateCreate.as_view(), name='template-create'),
    # url(r'^template/(?P<pk>\d+)$', views.___, name='template-view'),
    # url(r'^template/edit/(?P<pk>\d+)$', views.___, name='template-edit'),
    # url(r'^chart/create$', views.___, name='chart-create'),
    # url(r'^chart/(?P<pk>\d+)$', views.___, name='chart-view'),
    # url(r'^chart/edit/(?P<pk>\d+)$', views.___, name='chart-edt'),
)
