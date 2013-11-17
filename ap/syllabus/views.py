from django.views.generic import ListView, TemplateView, DetailView
from .models import Syllabus, Session

class AboutView(ListView):

	template_name = "syllabus/classlist.html"
	context_object_name = 'list'
	#allow_empty = True
	model = Syllabus
	#date_field = '' #Syllabus.classSyllabus.Term.start

	#allow_future = True

class SyllabusDetailView(ListView):
	model = Session
	template_name = "syllabus/detail.html"	
	context_object_name = 'sl'
	slug_field = 'classSyllabus'
	# slug_url_kwarg = 'code'
    



class HomeView(TemplateView):

	template_name = "syllabus/home.html"
	context_object_name = 'home'
	model = Syllabus
