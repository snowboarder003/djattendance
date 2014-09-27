import datetime

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from .models import ExamTemplate, Exam, TextQuestion, TextResponse


class ExamTemplateListView(ListView):
    template_name = 'exams/exam_template_list.html'
    model = ExamTemplate
    context_object_name = 'exam_templates'

    def get_queryset(self):
    	return ExamTemplate.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExamTemplateListView, self).get_context_data(**kwargs)
        return context

class SingleExamGradesListView(ListView):
	template_name = 'exams/single_exam_grades.html'
	model = Exam
	context_object_name = 'exam_grades'

	def get_context_data(self, **kwargs):
		context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
		context['exam_template_name'] = 'Exam Template Name'
		return context

class CreateExamView(CreateView):
	template_name = 'exams/take_single_exam.html'
	model = Exam
	fields = []
	context_object_name = 'exam'
	
	def get_context_data(self, **kwargs):
		context = super(CreateExamView, self).get_context_data(**kwargs)
		context['questions'] = self.questions
		return context