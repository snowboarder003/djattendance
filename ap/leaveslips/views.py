from django.views import generic
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import LeaveSlip, IndividualSlip, GroupSlip, MealOutSlip, NightOutSlip, IndividualSlipForm, GroupSlipForm, MealOutForm, NightOutForm
from accounts.models import Profile

# individual slips
class IndividualSlipCreate(generic.CreateView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_create.html'
    form_class = IndividualSlipForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        mealout_form = MealOutForm()
        nightout_form = NightOutForm()
        return self.render_to_response(
            self.get_context_data(form=form, mealout_form=mealout_form, nightout_form=nightout_form))

    def form_valid(self, form, mealout_form, nightout_form):
        if form.is_valid():
            # if self.object.type == 'MEAL':
            #     break
            # else:
            #     if self.object.type == 'NIGHT':
            #         break

			self.object = form.save(commit=False)
			self.object.status = 'P'
			self.object.trainee = Profile.get_trainee(self.request.user.id)
			self.object.TA = self.object.trainee.TA
			self.object.save()
			return super(generic.CreateView, self).form_valid(form)

    def form_invalid(self, form, mealout_form, nightout_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  mealout_form=mealout_form,
                                  nightout_form=nightout_form))


class IndividualSlipDetail(generic.DetailView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_detail.html'
    context_object_name = 'leaveslip'

class IndividualSlipUpdate(generic.UpdateView):
	model = IndividualSlip
	template_name = 'leaveslips/individual_update.html'
	form_class = IndividualSlipForm


# group slips
class GroupSlipCreate(generic.CreateView):
	model = GroupSlip
	template_name = 'leaveslips/group_create.html'
	form_class = GroupSlipForm

class GroupSlipDetail(generic.DetailView):
    model = GroupSlip
    template_name = 'leaveslips/group_detail.html'
    context_object_name = 'leaveslip'

# viewing the leave slips
class LeaveSlipList(generic.ListView):
    model = IndividualSlip
    template_name = 'leaveslips/list.html'

    def get_queryset(self):
        return IndividualSlip.objects.all # TODO: filter by user