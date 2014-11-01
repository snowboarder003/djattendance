import datetime

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect

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


