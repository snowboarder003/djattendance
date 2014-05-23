from django import forms
from lifestudies.models import LifeStudy, Summary

class NewSummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
    def save(self, commit=True):
        summary = super(NewSummaryForm, self).save(commit=False)
        if commit:
            summary.save()
        return summary

# class NewSyllabusForm(forms.ModelForm):
    
#     class Meta:
#         model = Syllabus

#     def save(self, commit=True):
#         syllabus = super(NewSyllabusForm, self).save(commit=False)
#         if commit:
#             syllabus.save()
#         return syllabus

# class NewSessionForm(forms.ModelForm):
#     class Meta:
#         model = Session
#     def save(self, commit=True):
#         session = super(NewSessionForm, self).save(commit=False)
#         if commit:
#             session.save()
#         return session

