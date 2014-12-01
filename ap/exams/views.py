import datetime

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages

from .models import ExamTemplate, Exam, TextQuestion, TextResponse


class ExamTemplateListView(ListView):
    template_name = 'exams/exam_template_list.html'
    model = ExamTemplate
    context_object_name = 'exam_templates'

    def get_queryset(self):
    	return ExamTemplate.objects.all()

    def get_context_data(self, **kwargs):
    	context = super(ExamTemplateListView, self).get_context_data(**kwargs)
    	context['taken'] = []
    	for template in ExamTemplate.objects.all():
    		context['taken'].append(template.is_taken(self.request.user.trainee))
    	return context

class SingleExamGradesListView(CreateView, SuccessMessageMixin):
	template_name = 'exams/single_exam_grades.html'
	model = ExamTemplate
	context_object_name = 'exam_grades'
	fields = []
	success_url = reverse_lazy('exams:exam_template_list')
	success_message = 'Exam grades updated.'

	def get_context_data(self, **kwargs):
		context = super(SingleExamGradesListView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		try:
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
			context['exams'] = []
		return context

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			grades = request.POST.getlist('exam-grade')
			exam_ids = request.POST.getlist('exam-id')
			for index, exam_id in enumerate(exam_ids):
				try:
					exam = Exam.objects.get(id=exam_id)
				except Exam.DoesNotExist:
					exam = False
				if exam:
					exam.grade = grades[index]
					exam.is_graded = True
					exam.save()
			messages.success(request, 'Exam grades saved.')
			return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))
		else:
			messages.add_message(request, messages.ERROR, 'Nothing saved.')
			return redirect('exams:exams_template_list')
		return HttpResponseRedirect(reverse_lazy('exams:exam_template_list'))

class GenerateGradeReport(DetailView):
	template_name = 'exams/exam_grade_report.html'
	model = Exam
	context_object_name = 'exam'
	fields = ['trainee', 'grade', 'exam_template', 'is_complete', 'is_graded']

	def get_context_data(self, **kwargs):
		context = super(GenerateGradeReport, self).get_context_data(**kwargs)
		return context

class GenerateRetakeList(DetailView):
	template_name = 'exams/exam_retake_list.html'
	model = ExamTemplate
	fields = []
	context_object_name = 'exam_template'

	def get_context_data(self, **kwargs):
		context = super(GenerateRetakeList, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		exam_stats = context['exam_template'].statistics()
		context['exam_max'] = exam_stats['maximum']
		context['exam_min'] = exam_stats['minimum']
		context['exam_average'] = exam_stats['average']
		try:
			context['exams'] = Exam.objects.filter(exam_template=context['exam_template']).order_by('trainee__account__lastname')
		except Exam.DoesNotExist:
			context['exams'] = []
		return context

class TakeExamView(SuccessMessageMixin, CreateView):
	template_name = 'exams/take_single_exam.html'
	model = Exam
	context_object_name = 'exam'
	fields = []
	success_url = reverse_lazy('exams:exam_template_list')
	success_message = 'Exam submitted successfully.'

	def get_context_data(self, **kwargs):
		context = super(TakeExamView, self).get_context_data(**kwargs)
		context['exam_template'] = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		context['exam_questions'] = context['exam_template'].questions.all()
		context['exam_is_taken'] = context['exam_template'].is_taken(self.request.user.trainee)
		return context

	def form_valid(self, form):
		exam = form.save(commit=False)
		template = ExamTemplate.objects.get(pk=self.kwargs['pk'])
		exam.exam_template = template
		exam.trainee = self.request.user.trainee
		exam.is_complete = True
		exam.save()

		responses = self.request.POST.getlist('response')
		questions = ExamTemplate.objects.get(pk=self.kwargs['pk']).questions.all()
		for i in range(len(responses)):
			new_response = TextResponse(body=responses[i], question=questions[i], exam=exam)
			new_response.save()
		return super(TakeExamView, self).form_valid(form)


