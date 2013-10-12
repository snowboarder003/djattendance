from django import forms
from absentTraineeRoster.models import Roster, Entry

class AbsentTraineeForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('absentee', 'reason', 'comments')