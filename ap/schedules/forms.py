from datetime import datetime
from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
import autocomplete_light

from .models import Event
from accounts.models import Trainee


class EventForm(forms.ModelForm):
    trainees = forms.ModelMultipleChoiceField(Trainee.objects.all(),
            required = False)

    class Meta:
        model = Event
        fields = ('type', 'name', 'code', 'description', 'classs', 'monitor', 'term', 'start', 'end')
        widgets = { 'start': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}),
                    'end': DateTimePicker(options={'format': 'MM/DD/YYYY HH:mm'}) }

