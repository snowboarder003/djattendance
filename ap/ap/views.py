from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views.generic.edit import FormView
# from ap.forms import AbsentTraineeForm

@login_required
def home(request):
    return render(request, 'index.html')

def base_example(request):
	return render(request, 'base_example.html')

# @login_required, permissions limited to HC's
# class AbsentTraineeRosterView(FormView):
# 	template_name = 'absentTraineeRoster.html'
# 	form_class = AbsentTraineeForm

# 	def form_valid(self, form):
# 		form.save()
# 		return super(AbsentTraineeRosterView, self).form)valid(form)
