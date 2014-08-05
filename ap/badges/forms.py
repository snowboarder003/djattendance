# forms.py
from django import forms
from .models import Badge

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        exclude = ('avatar',)

    def save(self, commit=True):
        badge = super(BadgeForm, self).save(commit=False)
        if commit:
            badge.save() #should also save the resizes avatar
        return badge

class BadgeUpdateForm(forms.ModelForm):
    class Meta:
        model = Badge
        exclude = ('avatar',)

    def save(self, commit=True):
        badge = super(BadgeUpdateForm, self).save(commit=False)
        if commit:
            badge.save()
        return badge

