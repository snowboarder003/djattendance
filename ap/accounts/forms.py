from accounts.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'phone',)


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
