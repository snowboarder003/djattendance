from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext 
from .models import Schedule, ScheduleTemplate, Event, EventGroup




class ScheduleCreateView(generic.CreateView):
    model = ScheduleTemplate
    template_name = 'schedules/new_schedule.html'
    fields = ['name']

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

	def get_queryset(self):
		return ScheduleTemplate.objects.all

# @login_required
def update_event(request):
	context = RequestContext(request)
	title = ''
	if request.method == 'GET':
		print request
		print request.GET

	# Do the update on the model here...

	return HttpResponse(request.GET['title'] + ' returned from view.')

# @login_required
def create_event(request):
	context = RequestContext(request)

	# create new EventGroup here and link it to the schedule

	return HttpResponse('Created new event... TODO.')