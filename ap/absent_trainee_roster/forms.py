from datetime import date

from django import forms

from absent_trainee_roster.models import Roster, Entry, Absentee
from accounts.models import Trainee


class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster


class AbsentTraineeForm(forms.ModelForm):
	comments = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'class':'comments form-control', 'placeholder':'Comments'}))


	class Meta:
		model = Entry
		fields = ('absentee', 'reason', 'coming_to_class', 'comments')

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(AbsentTraineeForm, self).__init__(*args, **kwargs)
		
		#Checks all the trainees in the same house as the user have an absentee profile and if not creates one
		for trainee in Trainee.objects.filter(account__trainee__house=self.user.trainee.house):
			obj, created = Absentee.objects.get_or_create(account=trainee.account)

		self.fields['absentee'].queryset = Absentee.objects.filter(account__trainee__house=self.user.trainee.house)
		self.fields['absentee'].label = 'Name'
		self.fields['absentee'].empty_label = '--Name--'
		self.fields['absentee'].widget.attrs={'class': 'form-control'}
		self.fields['reason'].widget.attrs={'class': 'form-control'}
	

class NewEntryFormSet(forms.models.BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(NewEntryFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted = True

	# need this function to get self.user
	def _construct_forms(self):
		self.forms = []
		for i in xrange(self.total_form_count()):
			self.forms.append(self._construct_form(i, user=self.user))
	
	def clean(self):
		#Checks that no two forms registers the same absentee.
		if any(self.errors):
			#Don't bother validating the formset unless each form is valid on its own
			return
		#roster = Roster.objects.filter(date=date.today())[0]
		#entries = Entry.objects.filter(roster=roster)
		absentees = [] # list of absentee id's
		for i in xrange(self.total_form_count()):
			if self.data['form-' + str(i) + '-absentee']:
				absentee = int(self.data['form-' + str(i) + '-absentee'])
				print('ABSENTEES', absentees)
				print('ABSENTEE', absentee)
				if absentee in absentees:
					raise forms.ValidationError("You're submitting multiple entries for the same trainee.")
				absentees.append(absentee)
		return super(NewEntryFormSet, self).clean()