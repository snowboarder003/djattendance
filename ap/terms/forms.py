from django import forms
from .models import Term
from .widgets import DatepickerWidget, HorizRadioRenderer

class NewTermForm(forms.ModelForm):
    
    class Meta:
        model = Term
        fields = ('season', 'start', 'end')
        widgets = {
            'season': forms.RadioSelect(renderer=HorizRadioRenderer),
            'start': DatepickerWidget(),
            'end': DatepickerWidget()
        }

    def save(self, commit=True):
        data = self.cleaned_data
        term = super(NewTermForm, self).save(commit=False)
        term.season = data['season']
        term.start = data['start']
        term.end = data['end']

        ## check if term code has duplicate??
        
        if commit:
            term.save()
        return term
