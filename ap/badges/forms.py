from django import forms
 
from .models import Badge
 
 
class UploadBadgeForm(forms.ModelForm):
     
    class Meta:
        model = Badge