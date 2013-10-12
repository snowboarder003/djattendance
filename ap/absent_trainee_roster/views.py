from django.shortcuts import render
from django.views.generic.edit import FormView
from absentTraineeRoster.forms import AbsentTraineeForm
	
def attendance_form(request):
	return render(request, 'absentTraineeRoster/attendance_form.html')

# @login_required, permissions limited to HC's
class AbsentTraineeFormView(FormView):
	template_name = 'absentTraineeRoster/absent_trainee_form.html'
	form_class = AbsentTraineeForm

	def form_valid(self, form):
		form.save()
		return super(AbsentTraineeRosterView, self).form_valid(form)