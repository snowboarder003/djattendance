from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView
from .models import Syllabus
from terms.models import Term
from django.shortcuts import render_to_response
from django.template import RequestContext




# class HomeView(ListView):
#     template_name = "syllabus/home.html"
#     model = Syllabus

class HomeView(ListView):
    template_name = "syllabus/termlist.html"
    model = Term
    context_object_name = 'termlist'

class TestView(ListView):
    template_name = "syllabus/detail.html"
    model = Syllabus
    context_object_name = 'syl_list'

class DetailView(ListView):
    template_name = "syllabus/details.html"
    model = Syllabus
    context_object_name = 'list'
    slug_url_kwarg = 'term','kode'
 
    def get_queryset(self):
        kode = self.kwargs['kode']
        term = self.kwargs['term']
        return Syllabus.objects.filter(classSyllabus__code= kode)
        # .filter(classSyllabus__term = term)




    

class AboutView(ListView):

    template_name = "syllabus/classlist.html"
    context_object_name = 'list'
    model = Syllabus



class SyllabusDetailView(ListView):
    model = Syllabus
    template_name = "syllabus/detail.html"  
    context_object_name = 'syllabus'
    slug_field = 'code'
    slug_url_kwarg = 'code'

