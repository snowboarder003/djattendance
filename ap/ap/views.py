from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from dailybread.models import Portion
from schedules.models import Schedule
from terms.models import Term
from accounts.models import Trainee

@login_required
def home(request):
    data = {'daily_nourishment': Portion.today(),
            'user': request.user}

    #check to see if an user is a trainee or a TA
    if hasattr(request.user, 'trainee'):
        try:
            data['schedule'] = request.user.trainee.schedule_set.get(term=Term.current_term())
        except ObjectDoesNotExist:
            pass
    elif hasattr(request.user, 'trainingassistant'):
        #do stuff to TA
        pass
    else:
        #do stuff to other kinds of users (anonymous?)
        pass

    return render(request, 'index.html', dictionary=data)

def base_example(request):
	return render(request, 'base_example.html')
