from django.views.generic import ListView, TemplateView, DetailView
from .models import Syllabus

class AboutView(ListView):

	template_name = "about.html"
	context_object_name = 'syllabus_list'
	#allow_empty = True
	model = Syllabus
	#date_field = '' #Syllabus.classSyllabus.Term.start

	#allow_future = True

class SyllabusDetailView(DetailView):
	model = Syllabus
	template_name = "detail.html"	

	""" TO DO: Get access to get_absolute_url from syllabus module """
	slug_field = 'get_absolute_url'
	slug_url_kwarg = 'get_absolute_url'

class HomeView(TemplateView):

	template_name = "home.html"
