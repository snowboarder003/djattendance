from django.conf.urls import patterns, url
from exams import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ExamTemplateListView.as_view(), name='exam_template_list'),
    url(r'^(?P<pk>\d+)/single-exam-grades$', views.SingleExamGradesListView.as_view(),
        name='single_exam_grades'),
    url(r'^$', views.CreateExamView.as_view(), name='take_exam'),
)
