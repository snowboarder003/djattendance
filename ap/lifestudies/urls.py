from django.conf.urls import patterns, url
from lifestudies.views import LifeStudyListView, CreateSummaryView

urlpatterns = patterns('',
    # ex: /lifestudies/
    url(r'^$', LifeStudyListView.as_view(), name='lifestudy-list'),
    # ex: /lifestudies/write/
    url(r'^(?P<pk>\d)/create_summary$', CreateSummaryView.as_view(), name='create-summary'),
    # url(r'^write/$', views.write, name='write'),
    # # ex: /lifestudies/result/
    # url(r'^result/$', views.result, name='result'),
)




