from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


from dailybread.models import Portion
from schedules.models import Schedule
from terms.models import Term

@login_required
def home(request):
    data = {'daily_nourishment': Portion.today(),
            'user': request.user}

    #test message
    messages.add_message(request, messages.DEBUG, 'DEBUG message')
    messages.add_message(request, messages.INFO, 'INFO message')
    messages.add_message(request, messages.SUCCESS, 'SUCCESS message')
    messages.add_message(request, messages.WARNING, 'WARNING message')
    messages.add_message(request, messages.ERROR, 'ERROR message')

    if request.user.trainee:
        try:
            data['schedule'] = request.user.trainee.schedule_set.get(term=Term.current_term())
        except ObjectDoesNotExist:
            pass

    return render(request, 'index.html', dictionary=data)

def base_example(request):
	return render(request, 'base_example.html')
