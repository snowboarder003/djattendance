from django import forms
from lifestudies.models import LifeStudy, Summary

class NewLifeStudyForm(forms.ModelFrom)
    class Meta:
        model = LifeStudy
    def save(self, commit=True):
        lifestudy = super(NewLifeStudyForm, self).save(commit=False)
        if commit:
            lifestudy.save()
        return lifestudy


class NewSummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
    def save(self, commit=True):
        summary = super(NewSummaryForm, self).save(commit=False)
        if commit:
            summary.save()
        return summary