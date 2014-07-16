from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dailybread.models import Portion

@login_required
def home(request):
    data = {'daily_nourishment': Portion.today()}
    return render(request, 'index.html', dictionary=data)

def base_example(request):
	return render(request, 'base_example.html')
