from django import forms

class UploadFileForm(forms.Form):
	file = forms.FileField()

class DisplayForm(forms.Form):
	outline = forms.CharField()