from django.views.generic import ListView, TemplateView
from .models import Syllabus

class AboutView(ListView):

	template_name = "syllabus/classlist.html"
	context_object_name = 'list'
	model = Syllabus

class SyllabusDetailView(ListView):
	model = Syllabus
	template_name = "syllabus/detail.html"	
	context_object_name = 'syllabus'
	slug_field = 'classSyllabus'
    
class HomeView(TemplateView):
	template_name = "syllabus/home.html"
	context_object_name = 'home'
	model = Syllabus
