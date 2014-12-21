from django import forms
from django_select2 import *

from .models import Trainee

class TraineeSelectForm(forms.Form):
    trainees = ModelSelect2MultipleField(queryset=Trainee.objects, required=False, search_fields=['^first_name', '^last_name'])