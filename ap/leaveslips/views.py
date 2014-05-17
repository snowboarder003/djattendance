from django.views import generic
from django.shortcuts import render

from .models import LeaveSlip, IndividualSlip, GroupSlip, MealOutSlip, NightOutSlip, IndividualSlipForm, GroupSlipForm

# individual slips
class IndividualSlipCreateView(generic.CreateView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_create.html'
    form_class = IndividualSlipForm

class IndividualSlipDetailView(generic.DetailView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_detail.html'

# group slips
class GroupSlipCreateView(generic.CreateView):
	model = GroupSlip
	template_name = 'leaveslips/group_create.html'
	form_class = GroupSlipForm

class GroupSlipDetailView(generic.DetailView):
    model = GroupSlip
    template_name = 'leaveslips/group_detail.html'