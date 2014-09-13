from django import forms
from accounts.models import Trainee

class NewAnnouncementForm(forms.Form):
	user = forms.ModelChoiceField(queryset=Trainee.objects.all(), required=False)
	send_to_all = forms.NullBooleanField()
	message = forms.CharField()

