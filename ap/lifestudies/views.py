from django.http import HttpResponse
from lifestudies.models import LifeStudy, Summary
from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
from accounts.models import User, Profile, Trainee, TrainingAssistant

class LifeStudyListView(ListView):
    template_name = 'lifestudies/lifestudylist.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    #profile is the user that's currently logged in
    def get_context_data(self, **kwargs):
        context = super(LifeStudyListView, self).get_context_data(**kwargs)
        if self.request.user is TrainingAssistant:
            context['ta'] = self.request.user.TrainingAssistant
        elif self.request.user is TrainingAssistant:
            context['trainee'] = self.request.user.Trainee
        return context

class SummaryCreateView(CreateView):
    model = Summary

    def get_success_url(self):
        return reverse_lazy('lifestudy-list')

class SummaryDetailView(DetailView):
    model = Summary
    context_object_name = 'summary'

# def lifestudy(request):
#     latest_summaries = LifeStudy.objects.order_by('offense')
#     output = ', '.join(["Life-Study Summary due as " + d.offense + " for " + d.infraction + " infraction ; " for d in latest_summaries])
#     return HttpResponse(output)

# def write(request):
#     response = "Life-Study Summary"
#     return HttpResponse(response)

# def result(request):
#     return HttpResponse("Your life-study summary has been successfully submitted.")