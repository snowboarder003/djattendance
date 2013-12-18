from django import forms
from django.forms.models import BaseInlineFormSet
from absent_trainee_roster.models import Entry, Roster
from datetime import date
from absent_trainee_roster.models import Roster, Entry, Absentee

class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster


class AbsentTraineeForm(forms.ModelForm):
	comments = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'class':'comments form-control', 'placeholder':'Comments'}))


	class Meta:
		model = Entry
		fields = ('absentee', 'reason', 'comments')

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(AbsentTraineeForm, self).__init__(*args, **kwargs)
		#Every trainee should have an absentee profile
		self.fields['absentee'].queryset = Absentee.objects.filter(account__trainee__house=self.user.trainee.house)
		self.fields['absentee'].label = 'Name'
		self.fields['absentee'].empty_label = '--Name--'
		self.fields['absentee'].widget.attrs={'class': 'form-control'}
		self.fields['reason'].widget.attrs={'class': 'form-control'}
	
"""
class BaseFormSet(BaseInlineFormSet):
	def save_new(self, form, commit=True):
		#custom save behaviour for new objects, form is a ModelForm
		return super(BaseFormSet, self).save_new(form, commit=commit)
	
	def save_existing(self, form, instance, commit=True):
		#custom save behaviour for existing objects
		#instance is the existing object, and form has the updated data
		return super(BaseFormset, self).save_existing(form, instance, commit=commit)
"""

class NewEntryFormSet(forms.models.ModelFormSet):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(NewEntryFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted =False

	def _construct_forms(self):
		self.forms = []
		for i in xrange(self.total_form_count()):
			self.forms.append(self._construct_form(i, user=self.user))
	
	def clean(self):
		#Checks that no two forms registers the same absentee.
		if any(self.errors):
			#Don't bother validating the formset unless each form is valid on its own
			return
		roster = Roster.objects.filter(date=date.today())[0]
		entries = Entry.objects.filter(roster=roster)
		absentees = []
		list = []
		for i in range(0, self.total_form_count()):
			form = self.forms[i]
			absentee = form.cleaned_data['absentee']
			#checks that absentee is not duplicated in formset
			if absentee in absentees:
				raise forms.ValidationError("You're submitting entries for the same trainee.")
			absentees.append(absentee)
			
			# checks that absentee is not already in roster
			for entry in entries:
				if absentee == entry.absentee:
					list.append(absentee)
		if list:
			raise forms.ValidationError("Entry/Entries for %s has already been submitted." %', '.join(map(str,list)))
			