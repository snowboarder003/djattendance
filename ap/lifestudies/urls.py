from django.conf.urls import patterns, url
from lifestudies.views import LifeStudyListView, LifeStudyCreateView, LifeStudyDetailView, \
                            SummaryCreateView, SummaryUpdateView, SummaryApproveView, ReportListView

urlpatterns = patterns('',
    url(r'^$', LifeStudyListView.as_view(), name='lifestudy-list'),
    url(r'^reportview$', ReportListView.as_view(), name='reportview'),
    url(r'^(?P<pk>\d+)/create_summary$', SummaryCreateView.as_view(), name='summary-create'),
    url(r'^(?P<pk>\d+)/detail_summary$', SummaryUpdateView.as_view(), name='summary-detail'),
    url(r'^(?P<pk>\d+)/approve_summary$', SummaryApproveView.as_view(), name='summary-approve'),
    url(r'^create_lifestudy$', LifeStudyCreateView.as_view(), name='lifestudy-create'),
    url(r'^(?P<pk>\d+)/detail_lifestudy$', LifeStudyDetailView.as_view(), name='lifestudy-detail'),
)




