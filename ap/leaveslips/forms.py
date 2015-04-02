from django import forms

from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee


class IndividualSlipForm(forms.ModelForm):
    class Meta:
        model = IndividualSlip
        fields = ['type', 'description', 'comments', 'texted', 'informed', 'events']


class GroupSlipForm(forms.ModelForm):
    class Meta:
        model = GroupSlip
        fields = ['type', 'trainees', 'description', 'comments', 'texted', 'informed', 'start', 'end']