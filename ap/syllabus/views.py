from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from syllabus.forms import NewSyllabusForm
from syllabus.models import Syllabus, Session
from classes.models import Class
from terms.models import Term
import ho.pisa as pisa
import cStringIO as StringIO
import cgi


class SyllabusListView(ListView):
    model = Syllabus
    template_name = "syllabus/syllabus_list.html"
    context_object_name = 'syllabi'

    def get_success_urlontext_data(self, **kwargs):
        context = super(SyllabusListView, self).get_context_data(**kwargs)
        context['term'] = self.kwargs['term']
        return context


class SyllabusDetailView(DetailView):
    template_name = "syllabus/syllabus_detail.html"
    model = Syllabus
    context_object_name = 'syllabus'
 
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


class SyllabusCreateView(CreateView):
    model = Syllabus
    template_name = 'syllabus/syllabus_form.html'
    form_class = NewSyllabusForm

    def get_success_url(self):
        return reverse_lazy('syllabus-list')


class SyllabusDeleteView(DeleteView):
    model = Syllabus
    template_name = 'syllabus/syllabus_delete.html'

    def get_success_url(self):
        return reverse_lazy('syllabus-list')


class SessionCreateView(CreateView):
    model = Session
    template_name = 'syllabus/session_form.html'

    def get_success_url(self):
        return reverse_lazy('syllabus-detail', kwargs={'pk': self.kwargs['syllabus_pk']})


class SessionDeleteView(DeleteView):
    model = Session
    template_name = 'syllabus/session_delete.html'

    def get_success_url(self):
        return reverse_lazy('syllabus-detail', kwargs={'pk': self.kwargs['syllabus_pk']})


class SessionDetailView(DetailView):
    model = Session
    template_name = 'syllabus/session_detail.html'
    context_object_name = 'session'

"""TODO: to display the sessions in chronological order in pdf"""
def pdf_view(request, syllabus_pk):
    syllabus = get_object_or_404(Syllabus, pk=syllabus_pk)
    return write_pdf('syllabus/syllabus_pdf.html',{
        'pagesize' : 'A4',
        'syllabus' : syllabus})


def write_pdf(template_src, template_context):
    template = get_template(template_src)
    context = Context(template_context)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(
        html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            mimetype='application/pdf')
    else:
        return http.HttpResponse('Yesh! %s' % cgi.escape(html))


