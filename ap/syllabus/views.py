from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, ArchiveIndexView, CreateView, DeleteView
from .models import Syllabus
from terms.models import Term
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import NewSyllabusForm
from django.core.urlresolvers import reverse_lazy




# class HomeView(ListView):
#     template_name = "syllabus/home.html"
#     model = Syllabus

class HomeView(ListView):
    template_name = "syllabus/termlist.html"
    model = Term
    context_object_name = 'termlist'

class CLView(ListView):
    template_name = "syllabus/classlist.html"
    context_object_name = 'list'
    model = Syllabus

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

class AddSyllabusView(CreateView):
    model = Syllabus
    template_name = 'syllabus/new_syllabus_form.html'
    form_class = NewSyllabusForm

'''TODO change this to DeleteView'''
class DeleteSyllabusView(ListView):
    model = Syllabus
    template_name = 'syllabus/delete_syllabus_confirm.html'
    #slug_field = 'after' # REPLACE_3
    #slug_url_kwarg = 'after' # REPLACE_4
    success_url = reverse_lazy('classlist-view') 

class TestView(ListView):
    template_name = "syllabus/detail.html"
    model = Syllabus
    context_object_name = 'syl_list'


class SyllabusDetailView(ListView):
    model = Syllabus
    template_name = "syllabus/detail.html"  
    context_object_name = 'syllabus'
    slug_field = 'code'
    slug_url_kwarg = 'code'

