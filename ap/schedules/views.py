from django.views import generic
from .models import Schedule, ScheduleTemplate, Event, EventGroup




class ScheduleCreateView(generic.CreateView):
    model = ScheduleTemplate
    template_name = 'schedules/new_schedule.html'
    fields = ['name']

class ScheduleListView(generic.ListView):
	model = ScheduleTemplate
	template_name = 'schedules/list.html'
	context_object_name = 'list_of_schedules'

	def get_queryset(self):
		return ScheduleTemplate.objects.all