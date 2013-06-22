from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ArchiveIndexView, DetailView, CreateView, DeleteView
from .models import Term
from .forms import NewTermForm

class IndexView(ArchiveIndexView):
    template_name = 'terms/index.html'
    context_object_name = 'term_list'
    model = Term
    date_field = 'start'

    allow_future = True

class TermDetailView(DetailView):
    model = Term
    template_name = 'terms/detail.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'

class AddTermView(CreateView):
    model = Term
    template_name = 'terms/new_term_form.html'
    form_class = NewTermForm

class DeleteTermView(DeleteView):
    model = Term
    template_name = 'terms/delete_term_confirm.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    success_url = reverse_lazy('terms:index')
