from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
# from ap.forms import AbsentTraineeForm


@login_required
def home(request):
    return render(request, 'index.html')