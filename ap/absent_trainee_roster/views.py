from django.forms.models import modelformset_factory
from django.shortcuts import render, render_to_response
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet
from absent_trainee_roster.models import Entry, Roster
from django.core.context_processors import csrf
from django.template import RequestContext
from datetime import date

def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=10, extra=2)
	if request.method == 'POST':
		formset = EntryFormSet(request.POST, request.FILES, user=request.user)
		if formset.is_valid():
			roster = Roster.objects.filter(date=date.today())[0]
			for form in formset.forms:
				entry = form.save(commit=False)
				entry.roster = roster
				entry.save()
	else:
		formset = EntryFormSet(user=request.user)

	c = {'formset': formset, 'user': request.user}
	c.update(csrf(request))

	return render_to_response('absent_trainee_roster/absent_trainee_form.html', c)
