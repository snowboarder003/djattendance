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

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        mealout_form = MealOutForm(self.request.POST)
        nightout_form = NightOutForm(self.request.POST)

        slip_type = self.request.POST['type']

        # working around the validation to make sure it passes based on type
        if ((slip_type == 'MEAL') and form.is_valid() and mealout_form.is_valid()):
                return self.form_valid(form, mealout_form, False)
        else:
            if ((slip_type == 'NIGHT') and form.is_valid() and nightout_form.is_valid()):
                return self.form_valid(form, False, nightout_form)
            else:
                if form.is_valid():
                    return self.form_valid(form, False, False)

        return self.form_invalid(form, mealout_form, nightout_form)


    def form_valid(self, form, mealout_form, nightout_form):
        self.object = form.save(commit=False)
        self.object.status = 'P'
        self.object.trainee = Profile.get_trainee(self.request.user.id)
        self.object.TA = self.object.trainee.TA
        self.object.save()

        if mealout_form:
            mealout = mealout_form.save(commit=False)
            mealout.leaveslip = self.object
            mealout.save()
        else:
            if nightout_form:
                nightout = nightout_form.save(commit=False)
                nightout.leaveslip = self.object
                nightout.save()

        return super(generic.CreateView, self).form_valid(form)

    def form_invalid(self, form, mealout_form, nightout_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  mealout_form=mealout_form,
                                  nightout_form=nightout_form))

class IndividualSlipUpdate(generic.UpdateView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_update.html'
    form_class = IndividualSlipForm

    # Does nothing right now, TODO
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(generic.edit.BaseUpdateView, self).get(request, *args, **kwargs)


class IndividualSlipDetail(generic.DetailView):
    model = IndividualSlip
    template_name = 'leaveslips/individual_detail.html'
    context_object_name = 'leaveslip'

    def get_context_data(self, **kwargs):
        context = super(IndividualSlipDetail, self).get_context_data(**kwargs)
        slip_id = kwargs['object'].id
        slip = IndividualSlip.objects.get(pk=slip_id)
        if slip.type == 'MEAL':
            slip = MealOutSlip.objects.get(leaveslip_id=slip_id)
            context['mealout_slip'] = slip
        else:
            if slip.type == 'NIGHT':
                slip = NightOutSlip.objects.get(leaveslip_id=slip_id)
                context['nightout_slip'] = slip

        return context

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