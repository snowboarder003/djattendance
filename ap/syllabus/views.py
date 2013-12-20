from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView
from .models import Syllabus




class HomeView(ListView):
    template_name = "syllabus/home.html"
    
    model = Syllabus

class DetailView(DetailView):
    model = Syllabus
    template_name = "syllabus/details.html"  
    slug_field = 'id'
    slug_url_kwarg = 'id'

    # def get_object():
    #     syllabus = Syllabus.objects.filter(classSyllabus__code= {{syllabus.classSyllabus.code}}).filter(classSyllabus__term__code={{syllabus.classSyllabus.term}})
    #     return syllabus




class AboutView(ListView):

    template_name = "syllabus/classlist.html"
    context_object_name = 'list'
    model = Syllabus

# class SyllabusDetailView(ListView):
#   model = Syllabus
#   template_name = "syllabus/detail.html"  
#   context_object_name = 'syllabus'
#   slug_field = 'classSyllabus'

class SyllabusDetailView(ListView):
    model = Syllabus
    template_name = "syllabus/detail.html"  
    context_object_name = 'syllabus'
    slug_field = 'code'
    slug_url_kwarg = 'code'






