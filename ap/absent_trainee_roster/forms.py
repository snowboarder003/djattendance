from django import forms
# from django_select2.fields import ModelSelect2Field
# from django_select2.widgets import Select2Widget
from absent_trainee_roster.models import Roster, Entry, Absentee
from absent_trainee_roster.widgets import AutocompleteWidget

class RosterForm(forms.ModelForm):
	class Meta:
		model = Roster


class AbsentTraineeForm(forms.ModelForm):
	comments = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'comments'}))

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
		super(AbsentTraineeForm, self).__init__(*args, **kwargs)
		self.fields['absentee'].queryset = Absentee.objects.filter(account__trainee__house=self.user.trainee.house)
		self.fields['absentee'].label = 'Name'
		self.fields['absentee'].empty_label = ''
		self.fields['absentee'].widget.attrs={'class': 'select2'}


class NewEntryFormSet(forms.formsets.BaseFormSet):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(NewEntryFormSet, self).__init__(*args, **kwargs)

	def _construct_forms(self):
		self.forms = []
		for i in xrange(self.total_form_count()):
			self.forms.append(self._construct_form(i, user=self.user))