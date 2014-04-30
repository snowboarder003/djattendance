from django import forms
from .models import Syllabus, Session
#from .widgets import DatepickerWidget, HorizRadioRenderer

class NewSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
 
    def save(self, commit=True):
        syllabus = super(NewSyllabusForm, self).save(commit=False)
        
        if commit:
            syllabus.save()
        return syllabus

"""TODO: to have multiple books"""
"""TODO: to have no books and no assignments if exam is selected"""
"""TODO: to display in order sorted by date"""
"""TODO: parse the assignments by comma but display them correctly"""
class NewSessionForm(forms.ModelForm):
    class Meta:
        model = Session

    def save(self, commit=True):
        session = super(NewSessionForm, self).save(commit=False)
        if commit:
            session.save()
        return session

