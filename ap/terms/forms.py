from django import forms
from .models import Term
from .widgets import DatepickerWidget

class NewTermForm(forms.ModelForm):
##    season = forms.ChoiceField(label='', choices=(('Spring', 'Spring'), ('Fall', 'Fall'),), widget=forms.RadioSelect)
    
    class Meta:
        model = Term
        fields = ('start', 'end')
        widgets = {
            'start': DatepickerWidget(attrs={'class':'datepicker'}),
            'end': DatepickerWidget(attrs={'class':'datepicker'})
        }

    def save(self, commit=True):
        data = self.cleaned_data
        term = super(NewTermForm, self).save(commit=False)
        term.start = data['start']
        term.end = data['end']
        if term.start.month == 2:
            if term.end.month == 7:
                term.name = 'Spring'
                term.code = 'Sp'
##            else:
                # error
        elif term.start.month == 8:
            if term.end.month == 12:
                term.name = 'Fall'
                term.code = 'Fa'
##            else:
                # error
##        else:
            # error
        if term.start.year == term.end.year:
            term.name += ' ' + str(term.start.year)
            term.code += str(term.start.year)[2:]
##        else:
            # error
        ## check if term code has duplicate
        
        if commit:
            term.save()
        return term
