from django.forms.models import modelformset_factory
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet
from django.shortcuts import render, render_to_response, redirect

from django.views.generic.edit import FormView
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet


from absent_trainee_roster.forms import AbsentTraineeForm
from absent_trainee_roster.models import Entry, Roster
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet

from datetime import date

from django.http import HttpResponse


def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=10, extra=1, can_delete=True)
	if request.method == 'POST':
		if Roster.objects.filter(date=date.today()).exists():
			roster = Roster.objects.get(date=date.today())
			formset = EntryFormSet(resquest.POST, instance=roster, user=request.user)
			
		else:
			roster = Roster.objects.create_roster(date=date.today())
			formset = EntryFormSet(request.POST, request.FILES, user=request.user)
			
		if formset.is_valid():
			for form in formset.forms:
				entry = form.save(commit=False)
				entry.roster = roster
				entry.save()
			roster.unreported_houses.remove(request.user.trainee.house)
			return redirect('/')
		
		else:
			c = {'formset': formset, 'user': request.user}
			c.update(csrf(request))
			
			return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)

	else:
		if Roster.objects.filter(date=date.today()).exists():
			roster = Roster.objects.get(date=date.today())
			formset = EntryFormSet(instance=roster, user=request.user)
		else:
			formset = EntryFormSet(user=request.user)

	c = {'formset': formset, 'user': request.user}
	c.update(csrf(request))

	return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)
