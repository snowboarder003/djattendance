from django.shortcuts import render
	
def attendance_form(request):
	return render(request, 'absent_trainee_roster/attendance_form.html')