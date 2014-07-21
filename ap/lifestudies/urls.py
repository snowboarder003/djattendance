from django.conf.urls import patterns, url
from .views import DisciplineListView, DisciplineCreateView, \
    DisciplineDetailView, SummaryCreateView, SummaryUpdateView, \
    SummaryApproveView, DisciplineReportView, CreateHouseDiscipline, \
    AttendanceAssign

urlpatterns = patterns(
    '',
    url(r'^$', DisciplineListView.as_view(), name='discipline_list'),
    url(r'^discipline-report$', DisciplineReportView.as_view(),
        name='discipline_report'),
    url(r'^(?P<pk>\d+)/create-summary$', SummaryCreateView.as_view(),
        name='summary_create'),
    url(r'^(?P<pk>\d+)/detail-summary$', SummaryUpdateView.as_view(),
        name='summary_detail'),
    url(r'^(?P<pk>\d+)/approve-summary$', SummaryApproveView.as_view(),
        name='summary_approve'),
    url(r'^create_discipline-house$', CreateHouseDiscipline.as_view(),
        name='discipline_house'),
    url(r'^create-discipline$', DisciplineCreateView.as_view(),
        name='discipline_create'),
    url(r'^(?P<pk>\d+)/detail-discipline$', DisciplineDetailView.as_view(),
        name='discipline_detail'),
    url(r'^(?P<period>\d+)/attendance-assign$', AttendanceAssign.as_view(),
        name='attendance_assign'),
)
