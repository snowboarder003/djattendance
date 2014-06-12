from django import forms
from lifestudies.models import LifeStudy, Summary
from houses.models import House


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
        exclude = ('approved', 'lifeStudy',)
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


class HouseLifeStudyForm(forms.ModelForm):
    class Meta:
        model = LifeStudy
        exclude = ('trainee')
    House = forms.ModelChoiceField(House.objects)
    

"""
class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['sku'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.sku
        else:
            return self.cleaned_data['sku']

"""


