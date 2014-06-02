from django import forms
from lifestudies.models import LifeStudy, Summary


class NewLifeStudyForm(forms.ModelForm):
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
        exclude = ('approved',)
    def save(self, commit=True):
        summary = super(NewSummaryForm, self).save(commit=False)
        if commit:
            summary.save()
        return summary


class EditSummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        exclude = ('book','chapter','lifeStudy','approved',)
    def save(self, commit=True):
        summary = super(EditSummaryForm, self).save(commit=False)
        if commit:
            summary.save()
        return summary