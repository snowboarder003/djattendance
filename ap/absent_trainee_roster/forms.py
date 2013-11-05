from django import forms
# from django_select2.fields import ModelSelect2Field
# from django_select2.widgets import Select2Widget
from absent_trainee_roster.models import Roster, Entry, Absentee

class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster


class AbsentTraineeForm(forms.ModelForm):
	comments = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'class':'comments'}))

	class Meta:
		model = Entry
		fields = ('absentee', 'reason', 'comments')
		# widgets = {
		# 	'absentee': Select2Widget(select2_options={
		# 		'width':'element',
		# 		}),
		# }

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		print('ASDFASDFASDFASDFASDFASF USER')
		print(self.user)
		super(AbsentTraineeForm, self).__init__(*args, **kwargs)
		#Every trainee should have an absentee profile
		self.fields['absentee'].queryset = Absentee.objects.filter(account__trainee__house=self.user.trainee.house)
		self.fields['absentee'].label = 'Name'
		self.fields['absentee'].empty_label = ''
		self.fields['absentee'].widget.attrs={'class': 'select2'}


class NewEntryFormSet(forms.formsets.BaseFormSet):
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
		"""Checks that no two entries registers the same absentee."""
		if any(self.errors):
			#Don't bother validating the formset unless each form is valid on its own
			return
		absentees = []
		for i in range(0, self.total_form_count()):
			form = self.forms[i]
			absentee = form.cleaned_data['absentee']
			if absentee in absentees:
				raise forms.ValidationError("Entry for this absentee has already been submitted.")
			absentees.append(absentee)
		