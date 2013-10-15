from django.forms.models import modelformset_factory
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView
from absent_trainee_roster.forms import AbsentTraineeForm
from absent_trainee_roster.models import Entry
	
# @login_required, permissions limited to HC's
class AbsentTraineeFormView(FormView):
	template_name = 'absent_trainee_roster/absent_trainee_form.html'
	form_class = AbsentTraineeForm

	def form_valid(self, form):
		form.save()
		return super(AbsentTraineeFormView, self).form_valid(form)

def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, max_num=10, extra=2)
	if request.method == 'POST':
		formset = EntryFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			# do something with formset.cleaned_data
	else:
		formset = EntryFormSet()
	return render_to_response('absent_trainee_roster/absent_trainee_form.html', {'formset': formset, 'user':request.user})
