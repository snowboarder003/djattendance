from django.conf.urls import patterns, url
from lifestudies import views

urlpatterns = [
    # ex: /discipline/
    url(r'^$', views.lifestudy, name='lifestudy'),
    # ex: /discipline/write/
    url(r'write/$', views.write, name='write'),
    # ex: /discpline/result/
    url(r'result/$', views.result, name='result'),
]


