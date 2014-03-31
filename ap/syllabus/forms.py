from django import forms
from .models import Syllabus
#from .widgets import DatepickerWidget, HorizRadioRenderer

class NewSyllabusForm(forms.ModelForm):
    
    '''TODO: need to change the Fa|Sp\d{2} thing for each syllabus added
    apparently they all get added with Fa13,perhaps to overwrite 
    syllabus.classSyllabus.term or just fix the model'''
    class Meta:
        model = Syllabus
        #fields = ('season', 'start', 'end')
        #widgets = {
        #    'season': forms.RadioSelect(renderer=HorizRadioRenderer),
        #    'start': DatepickerWidget(),
        #    'end': DatepickerWidget()
        #}

    def save(self, commit=True):
        #data = self.cleaned_data
        syllabus = super(NewSyllabusForm, self).save(commit=False)
        #syllabus.season = data['season']
        #syllabus.name = data['season']
        #syllabus.code = syllabus.name[:2]
        #syllabus.start = data['start']
        #syllabus.end = data['end']

        #if syllabus.start.year == syllabus.end.year:
        #    syllabus.name += ' ' + str(syllabus.start.year)
        #    syllabus.code += str(syllabus.start.year)[2:]
##        else:
            # error
        ## check if term code has duplicate??
        
        if commit:
            syllabus.save()
        return syllabus


