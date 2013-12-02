from django.views.generic import ListView, TemplateView
from .models import Syllabus, Session

class AboutView(ListView):

	template_name = "syllabus/classlist.html"
	context_object_name = 'list'
	model = Syllabus

class SyllabusDetailView(ListView):
	model = Syllabus
	template_name = "syllabus/detail.html"	
	context_object_name = 'syllabus'
	slug_field = 'classSyllabus'

	# trying to get access to the SYLABBUS model somehow along with the SESSION model
	#def get_context_data(self, **kwargs):
	#    context = super(SyllabusDetailView, self).get_context_data(**kwargs)
	#    context['more_model_objects'] = Syllabus.objects.all()
	#    return context
    
class HomeView(TemplateView):
	template_name = "syllabus/home.html"
	context_object_name = 'home'
	model = Syllabus
