from django.forms.models import modelformset_factory
from absent_trainee_roster.forms import AbsentTraineeForm, NewEntryFormSet
from django.shortcuts import render, render_to_response, redirect
from absent_trainee_roster.models import Entry, Roster
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from datetime import date
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def absent_trainee_form(request):
	EntryFormSet = modelformset_factory(Entry, AbsentTraineeForm, formset=NewEntryFormSet, max_num=10, extra=2, can_delete=True)
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
			roster.unreported_houses.remove(request.user.trainee.house)
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

# def pdf_helloworld(request):
# 	# Create the HttpResponse object with the appropriate PDF headers.
# 	response = HttpResponse(content_type='application/pdf')
# 	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

# 	# Create the PDF object, using the response object as its "file."
# 	pdf = canvas.Canvas(response)

# 	# Draw things on the PDF. Here's where the PDF generation happens.
# 	# See the ReportLab documentation for the full list of functionality.
# 	p.drawString(100, 100, "Hello world.")

# 	# Close the PDF object cleanly, and we're done.
# 	p.showPage()
# 	p.save()
# 	return response
