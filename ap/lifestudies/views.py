from django.http import HttpResponse
from lifestudies.models import LifeStudy, Summary
from django.views.generic import ListView, CreateView, DetailView, FormView
from lifestudies.forms import NewSummaryForm, NewLifeStudyForm
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView
from lifestudies.forms import NewSummaryForm, EditSummaryForm
from django.core.urlresolvers import reverse_lazy
from accounts.models import User, Profile, Trainee, TrainingAssistant

class LifeStudyListView(ListView):
    template_name = 'lifestudies/lifestudylist.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    #this function is called whenever 'post'
    def post(self, request, *args, **kwargs):
        #turning the 'post' into a 'get'
        return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(LifeStudyListView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        if self.request.method == 'POST':
            for lifestudy in context['object_list']:
                if lifestudy.pk in self.request.POST:
                    lifestudy.approveAllSummary
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
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_detail.html'
    fields = ['content']
    form_class = EditSummaryForm
    
    myform.fields['status'].widget.attrs['readonly'] = True
    
    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(SummaryDetailView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        if self.request.method == 'POST':
            for summary in context['object_list']:
                if summary.pk in self.request.POST:
                    summary.approve
        return context

    def get_success_url(self):
        return reverse_lazy('lifestudy-list')

"""
    def approve(request):
        if request.method == "POST":
            form = ApproveSummaryForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('lifestudies/lifestudylist.html')
        else:
            form = ApproveSummaryForm()

        return render(request, 'summary_detail.html', {'form':form,
        })
"""
