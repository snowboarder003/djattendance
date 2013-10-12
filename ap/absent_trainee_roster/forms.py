from django import forms
from absent_trainee_roster.models import Roster, Entry

class AbsentTraineeForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('absentee', 'reason', 'comments')