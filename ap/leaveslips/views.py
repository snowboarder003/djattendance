from django.views import generic
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import LeaveSlip, IndividualSlip, GroupSlip, IndividualSlipForm, GroupSlipForm
from accounts.models import Profile

from itertools import chain
from datetime import datetime

# individual slips
class IndividualSlipCreate(generic.CreateView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_create.html'
    form_class = IndividualSlipForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = 'P'
        self.object.trainee = Profile.get_trainee(self.request.user.id)
        self.object.TA = self.object.trainee.TA
        self.object.save()
        return super(generic.CreateView, self).form_valid(form)

class IndividualSlipDetail(generic.DetailView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_detail.html'
    context_object_name = 'leaveslip'

class IndividualSlipUpdate(generic.UpdateView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_update.html'
    form_class = IndividualSlipForm

class IndividualSlipDelete(generic.DeleteView):
    model = IndividualSlip
    # template_name = 'leaveslips/'
    form_class = IndividualSlipForm

# group slips
class GroupSlipCreate(generic.CreateView):
	model = GroupSlip
	template_name = 'leaveslips/group_create.html'
	form_class = GroupSlipForm

        def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.status = 'P'
            self.object.trainee = Profile.get_trainee(self.request.user.id)
            self.object.TA = self.object.trainee.TA
            self.object.save()
            return super(generic.CreateView, self).form_valid(form)


class GroupSlipDetail(generic.DetailView):
    model = GroupSlip
    template_name = 'leaveslips/group_detail.html'
    context_object_name = 'leaveslip'

class GroupSlipUpdate(generic.UpdateView):
    model = GroupSlip
    template_name = 'leaveslips/group_update.html'
    form_class = GroupSlipForm

class GroupSlipDelete(generic.DeleteView):
    model = GroupSlip
    # template_name = 'leaveslips/'
    form_class = GroupSlipForm

# viewing the leave slips
class LeaveSlipList(generic.ListView):
    model = IndividualSlip, GroupSlip
    template_name = 'leaveslips/list.html'


    def get_queryset(self):
         individual=IndividualSlip.objects.filter(trainee=self.request.user.id)
         group=GroupSlip.objects.filter(trainee=self.request.user.id)
         queryset= chain(individual,group) #combines two querysets
         return queryset
