from django.http import HttpResponse, HttpResponseRedirect
from lifestudies.models import LifeStudy, Summary
from accounts.models import User, Profile, Trainee, TrainingAssistant
from lifestudies.forms import NewSummaryForm, NewLifeStudyForm, EditSummaryForm
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView
from django.core.urlresolvers import reverse_lazy

class LifeStudyListView(ListView):
    template_name = 'lifestudies/lifestudylist.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    #this function is called whenever 'post'
    def post(self, request, *args, **kwargs):
        for value in request.POST.getlist('approve_selected'):
            print LifeStudy.objects.get(pk=value).approveAllSummary()
        return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(LifeStudyListView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        # if self.request.method == 'POST':
        #     for lifestudy in context['object_list']:
        #         if lifestudy.pk in self.request.POST:
        #             lifestudy.approveAllSummary
        return context


class ReportListView(ListView):
    template_name = 'lifestudies/reportview.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    #this function is called whenever 'post'
    def post(self, request, *args, **kwargs):
        #turning the 'post' into a 'get'
        return self.get(request, *args, **kwargs)

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
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

    def get_context_data(self, **kwargs):
        context = super(SummaryCreateView, self).get_context_data(**kwargs)
        return context 

    def form_valid(self, form):
        form.lifeStudy = self.kwargs['pk']
        return HttpResponseRedirect(self.get_success_url())

"""this is the view that TA will click into when viewing a summary and approving it"""
class SummaryApproveView(DetailView):
    model = Summary
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_approve.html'

    def post(self, request, *args, **kwargs):
        self.get_object().approve()
        return HttpResponseRedirect(reverse_lazy('lifestudy-list'))


"""this is the view that trainee click into in order to update the content of the summary"""
class SummaryUpdateView(UpdateView):
    model = Summary
    context_object_name = 'summary'
    template_name = 'lifestudies/summary_detail.html'
    fields = ['content']
    form_class = EditSummaryForm
        
    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(SummaryUpdateView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        print(self.request.POST)
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
