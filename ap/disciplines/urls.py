from django.conf.urls import patterns, url
from disciplines import views

urlpatterns = [
    # ex: /discipline/
    url(r'^$', views.discipline, name='discipline'),
    # ex: /discipline/write/
    url(r'write/$', views.write, name='write'),
    # ex: /discpline/result/
    url(r'result/$', views.result, name='result'),
]