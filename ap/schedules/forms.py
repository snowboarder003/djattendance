from datetime import datetime
from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
import autocomplete_light

from .models import Event
from accounts.models import Trainee


class EventForm(forms.ModelForm):
    trainees = forms.ModelMultipleChoiceField(Trainee.objects.all(), 
            widget = autocomplete_light.MultipleChoiceWidget('TraineeAutocomplete'),
            required = False)

    class Meta:
        model = Event
        fields = ('type', 'name', 'code', 'description', 'classs', 'monitor', 'term', 'start', 'end')
        widgets = { 'start': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
                    'end': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}) }

    # def clean_start(self):
    # 	data = self.cleaned_data['start']
    # 	if data[-2:] == 'AM':
    # 		return data[:-3]
    # 	elif data[-2:] == 'PM':
    # 		if len(data) == 18: # hour has one digit
    # 			hour = int(data[11]) + 12
    # 		elif len(data) == 19: # hour has two digits
    # 			hour = int(data[11:13])
    # 		else:
    # 			raise forms.ValidationError('Please enter date in format "MM/DD/YYYY HH:MM A/PM".')
    # 		hour += 12
    # 		return data[:11] + str(hour) + data[-3:]
