from django.conf.urls import patterns, url
from lifestudies.views import LifeStudyListView

urlpatterns = patterns('',
    # ex: /lifestudies/
    url(r'^$', LifeStudyListView.as_view(), name='lifestudy-list'),
    # ex: /lifestudies/write/
    # url(r'^write/$', views.write, name='write'),
    # # ex: /lifestudies/result/
    # url(r'^result/$', views.result, name='result'),
)




