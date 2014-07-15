from accounts.models import User
from django import forms

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def __init__(self, *args, **kw):
        super(UserForm, self).__init__(*args, **kw)
        self.fields['firstname'].initial = self.instance.user.firstname
        self.fields['lastname'].initial = self.instance.user.lastname

        self.fields.keyOrder = [
            'firstname',
            'lastname',
            ]

    def save(self, *args, **kw):
        super(UserForm, self).save(*args, **kw)
        self.instance.user.first_name = self.cleaned_data.get('firstname')
        self.instance.user.last_name = self.cleaned_data.get('lastname')
        self.instance.user.save()

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password')


class EmailForm(forms.ModelForm):
    email = forms.CharField(max_length=255)
    email_confirmation = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('email',)
