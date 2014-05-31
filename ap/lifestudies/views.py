from django.http import HttpResponse
from lifestudies.models import LifeStudy, Summary
<<<<<<< HEAD
from django.views.generic import ListView, CreateView, DetailView, FormView
from lifestudies.forms import NewSummaryForm, NewLifeStudyForm
=======
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView
from lifestudies.forms import NewSummaryForm, EditSummaryForm
>>>>>>> e83746d405ce2e67eeff42055fefe315c5eac89f
from django.core.urlresolvers import reverse_lazy
from accounts.models import User, Profile, Trainee, TrainingAssistant

class LifeStudyListView(ListView):
    template_name = 'lifestudies/lifestudylist.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(LifeStudyListView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context


class LifeStudyCreateView(CreateView):
    model = LifeStudy
    form_class = NewLifeStudyForm

    def get_success_url(self):
        return reverse_lazy('lifestudy-list')


class LifeStudyDetailView(DetailView):
    model = LifeStudy
    context_object_name = 'lifestudy'


class SummaryCreateView(CreateView):
    model = Summary
    form_class = NewSummaryForm

    def get_success_url(self):
        return reverse_lazy('lifestudy-list')


class SummaryDetailView(UpdateView):
    model = Summary
<<<<<<< HEAD
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_detail.html'

=======
    fields = ['content']
    template_name = 'lifestudies/summary_detail.html'
    form_class = EditSummaryForm
>>>>>>> e83746d405ce2e67eeff42055fefe315c5eac89f

    def get_success_url(self):
        return reverse_lazy('lifestudy-list')
