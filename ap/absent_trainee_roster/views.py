from django.forms.models import modelformset_factory
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.edit import FormView
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponse

from absent_trainee_roster.forms import AbsentTraineeForm
from absent_trainee_roster.models import Entry, Roster
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet
from datetime import date


def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=10)
	if request.method == 'POST':
		try:
			roster = Roster.objects.filter(date=date.today())[0]
		except Exception as e:
			return HttpResponse("Roster was not created for today.")
			
		formset = EntryFormSet(request.POST, request.FILES, user=request.user)
		if formset.is_valid():
			for form in formset.forms:
				entry = form.save(commit=False)
				entry.roster = roster
				entry.save()
			return redirect('/')
		
		else:
			
			c = {'formset': formset, 'user': request.user}
			c.update(csrf(request))
			
			return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)
	else:
		formset = EntryFormSet(user=request.user)

	c = {'formset': formset, 'user': request.user}
	c.update(csrf(request))

	return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)

