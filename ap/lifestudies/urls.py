from django.conf.urls import patterns, url
from lifestudies.views import LifeStudyListView, SummaryCreateView, SummaryDetailView

urlpatterns = patterns('',
    url(r'^$', LifeStudyListView.as_view(), name='lifestudy-list'),
    url(r'^(?P<pk>\d)/create_summary$', SummaryCreateView.as_view(), name='summary-create'),
    url(r'^(?P<pk>\d)/detail_summary$', SummaryDetailView.as_view(), name='summary-detail'),
    # url(r'^write/$', views.write, name='write'),
    # # ex: /lifestudies/result/
    # url(r'^result/$', views.result, name='result'),
)




