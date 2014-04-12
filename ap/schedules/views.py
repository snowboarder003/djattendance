from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext 
from django.forms.models import modelform_factory

from .models import Schedule, ScheduleTemplate, Event, EventGroup
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget


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
    

class ScheduleCreate(generic.CreateView):
    model = ScheduleTemplate
    template_name = 'schedules/new_schedule.html'
    fields = ['name']

<<<<<<< HEAD
class ScheduleDetailView(generic.DetailView):
	model = Schedule
	template_name = 'schedules/view.html'

	def get_context_data(self, **kwargs):
		context = super(ScheduleDetailView, self).get_context_data(**kwargs)
		return context

class ScheduleListView(generic.ListView):
	model = ScheduleTemplate
	template_name = 'schedules/list.html'
	context_object_name = 'list_of_schedules'
=======
>>>>>>> 92597d4d489268650907682efec1155750f14b01

class ScheduleList(generic.ListView):
    model = ScheduleTemplate
    template_name = 'schedules/list.html'
    context_object_name = 'list_of_schedules'

    def get_queryset(self):
        return ScheduleTemplate.objects.all


<<<<<<< HEAD
	return HttpResponse(request.GET['title'] + ' returned from view.')

# @login_required
def create_event(request):
	context = RequestContext(request)

	# create new EventGroup here and link it to the schedule

	return HttpResponse('Created new event... TODO.')
=======
>>>>>>> 92597d4d489268650907682efec1155750f14b01
