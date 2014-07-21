from django.http import HttpResponse, HttpResponseRedirect
from lifestudies.models import Discipline, Summary
from accounts.models import User, Profile, Trainee, TrainingAssistant
from lifestudies.forms import NewSummaryForm, NewDisciplineForm, \
    EditSummaryForm, HouseDisciplineForm
from django.views.generic import ListView, CreateView, DetailView, FormView, \
    UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from terms.models import Term
from attendance.utils import Period
from schedules.models import Schedule
from teams.models import Team
from houses.models import House
from books.models import Book
import datetime
import logging

from django.db import transaction

logger = logging.getLogger(__name__)


class DisciplineListView(ListView):
    template_name = 'lifestudies/discipline_list.html'
    model = Discipline
    context_object_name = 'disciplines'

    def post(self, request, *args, **kwargs):
        """'approve' when an approve button is pressed 'delete' when a delete
        button is pressed 'attend_assign' when assgning discipline from
        AttendanceAssign"""
        if 'approve' in request.POST:
            for value in request.POST.getlist('selection'):
                Discipline.objects.get(pk=value).approve_all_summary()
        if 'delete' in request.POST:
            for value in request.POST.getlist('selection'):
                Discipline.objects.get(pk=value).delete()
        if 'attendance_assign' in request.POST:
            period = int(request.POST.get('attendance_assign'))
            for trainee in Trainee.objects.all():
                num_summary = Discipline.calculate_summary(trainee, period)
                if num_summary > 0:
                    discipline = Discipline(infraction='attendance',
                                            quantity=num_summary,
                                            due=Period().end(period),
                                            offense='MO',
                                            trainee=trainee)
                    try:
                        discipline.save()
                    except IntegrityError:
                        logger.error('Abort trasanction error')
                        transaction.rollback()
        return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(DisciplineListView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        current_date = datetime.datetime.now().date()
        context['current_period'] = Period(Term.objects.get(pk=4)).period_of_date(datetime.date(2014,06,06))
        return context


class DisciplineReportView(ListView):
    template_name = 'lifestudies/discipline_report.html'
    model = Discipline
    context_object_name = 'disciplines'

    #this function is called whenever 'post'
    def post(self, request, *args, **kwargs):
        #turning the 'post' into a 'get'
        return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(DisciplineReportView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        context['trainees'] = Trainee.objects.all()
        context['teams'] = Team.objects.all()
        context['houses'] = House.objects.all()
        if self.request.method == 'POST':
            for discipline in context['object_list']:
                if discipline.pk in self.request.POST:
                    discipline.approve_all_summary
        return context


class DisciplineCreateView(CreateView):
    model = Discipline
    form_class = NewDisciplineForm

    def get_success_url(self):
        return reverse_lazy('discipline-list')


class DisciplineDetailView(DetailView):
    model = Discipline
    context_object_name = 'discipline'
    template_name = 'lifestudies/discipline_detail.html'

    def post(self, request, *args, **kwargs):
        if 'summary_pk' in request.POST:
            approve_summary_pk = int(request.POST['summary_pk'])
            Summary.objects.get(pk=approve_summary_pk).approve()
        if 'hard_copy' in request.POST:
            self.get_object().summary_set.create(
                content='approved hard copy summary',
                book=Book.objects.get(pk=1),
                chapter=1,
                approved=True)
        return HttpResponseRedirect('')


class SummaryCreateView(CreateView):
    model = Summary
    form_class = NewSummaryForm

    def get_success_url(self):
        return reverse_lazy('discipline-list')

    def get_context_data(self, **kwargs):
        context = super(SummaryCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        summary = form.save(commit=False)
        summary.discipline = Discipline.objects.get(pk=self.kwargs['pk'])
        summary.date_submitted = datetime.datetime.now()
        summary.save()
        return super(SummaryCreateView, self).form_valid(form)


class SummaryApproveView(DetailView):
    """this is the view that TA will click into when viewing a summary and
    approving it"""
    model = Summary
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_approve.html'

    def post(self, request, *args, **kwargs):
        self.get_object().approve()
        return HttpResponseRedirect(reverse_lazy('discipline-list'))


class SummaryUpdateView(UpdateView):
    """this is the view that trainee click into in order to update the
    content of the summary"""
    model = Summary
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_detail.html'
    fields = ['content']
    form_class = EditSummaryForm

    def get_context_data(self, **kwargs):
        context = super(SummaryUpdateView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context

    def get_success_url(self):
        return reverse_lazy('discipline-list')


class CreateHouseDiscipline(TemplateView):
    template_name = 'lifestudies/discipline_house.html'

    def get_context_data(self, **kwargs):
        context = super(CreateHouseDiscipline, self).get_context_data(**kwargs)
        context['form'] = HouseDisciplineForm()
        return context

    def post(self, request, *args, **kwargs):
        """this manually creates Disciplines for each house member"""
        if request.method == 'POST':
            form = HouseDisciplineForm(request.POST)
            if form.is_valid():
                listTrainee = form.cleaned_data['House'].trainee_set.all()
                for trainee in listTrainee:
                    discipline = Discipline(
                        infraction=form.cleaned_data['infraction'],
                        quantity=form.cleaned_data['quantity'],
                        due=form.cleaned_data['due'],
                        offense=form.cleaned_data['offense'],
                        trainee=trainee)
                    try:
                        discipline.save()
                    except IntegrityError:
                        transaction.rollback()

                return HttpResponseRedirect(reverse_lazy('discipline-list'))
        else:
            form = HouseDisciplineForm()
        return HttpResponseRedirect(reverse_lazy('discipline-list'))


class AttendanceAssign(ListView):
    """this view mainly displays trainees, their roll status, and the number
     of summary they are to be assigned. The actual assigning is done by
    DisciplineListView"""
    model = Trainee
    template_name = 'lifestudies/attendance_assign.html'
    context_object_name = 'trainees'

    def get_context_data(self, **kwargs):
        """this adds outstanding_trainees, a dictionary
        {trainee : num_summary} for the template to display the trainees who
        need will have outstanding summaries"""
        context = super(AttendanceAssign, self).get_context_data(**kwargs)
        period = int(self.kwargs['period'])
        context['period'] = period
        context['start_date'] = Period().start(period)
        context['end_date'] = Period().end(period)
        context['outstanding_trainees'] = {}
        for trainee in Trainee.objects.all():
            num_summary = Discipline.calculate_summary(trainee, period)
            if num_summary > 0:
                context['outstanding_trainees'][trainee] = num_summary
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            period = int(request.POST['select_period'])
            return HttpResponseRedirect(reverse_lazy('attendance-assign',
                                                     kwargs={'period': period})
                                        )
        else:
            return HttpResponseRedirect(reverse_lazy('attendance-assign',
                                                     kwargs={'period: 1'}))
