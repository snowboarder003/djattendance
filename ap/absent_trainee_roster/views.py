from django.shortcuts import render
from django.views.generic.edit import FormView
from absent_trainee_roster.forms import AbsentTraineeForm
	
def absent_trainee_form(request):
	return render(request, 'absent_trainee_roster/absent_trainee_form.html')

# @login_required, permissions limited to HC's
class AbsentTraineeFormView(FormView):
	template_name = 'absent_trainee_roster/absent_trainee_form.html'
	form_class = AbsentTraineeForm

	def form_valid(self, form):
		form.save()
		return super(AbsentTraineeFormView, self).form_valid(form)