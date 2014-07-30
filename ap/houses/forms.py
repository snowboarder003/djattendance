from django.forms import Form
from django import forms
from accounts.models import Trainee

class BunkForm(Form):
	trainee = forms.ModelChoiceField(queryset=Trainee.objects.all())
