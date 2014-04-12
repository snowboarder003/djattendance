from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib.admin.widgets import AdminDateWidget

from .models import Schedule, ScheduleTemplate, Event, EventGroup
from terms.models import Term


class ScheduleDetail(generic.DetailView):
    model = Schedule
    template_name = 'schedules/schedule_detail.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        if not self.args:
            self.user = self.request.user
        else:
            self.user = get_object_or_404(User, pk=self.args[0])
        return Schedule.objects.filter(trainee=self.user.trainee).filter(term=Term.current_term())

class ScheduleCreate(generic.CreateView):
    model = ScheduleTemplate
    template_name = 'schedules/new_schedule.html'
    fields = ['name']


class ScheduleList(generic.ListView):
    model = ScheduleTemplate
    template_name = 'schedules/list.html'
    context_object_name = 'list_of_schedules'

    def get_queryset(self):
        return ScheduleTemplate.objects.all

class EventCreate(generic.CreateView):
    model = Event
    fields = ['name', 'code', 'description', 'group', 'classs', 'type', 'date', 'start', 'end']
    template_name = 'schedules/event_create.html'
    form_class =  modelform_factory(Event,
                                    widgets = { "date": AdminDateWidget() })
    success_url = reverse_lazy('event-create')


class EventDetail(generic.DetailView):
    model = Event
    context_object_name = "event"


class EventUpdate(generic.UpdateView):
    model = Event
    template_name = 'schedules/event_update.html'


class EventDelete(generic.DeleteView):
    model = Event
    success_url = reverse_lazy('event-create')
