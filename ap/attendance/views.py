from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404

from .models import Roll, Period
from schedules.models import Schedule, Event
from terms.models import Term
from accounts.models import User


class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'attendance'

    def get_context_data(self, **kwargs):
        context = super(AttendancePersonal, self).get_context_data(**kwargs)
        context['trainee'] = self.request.user.trainee
        context['schedule'] = Schedule.objects.filter(term=Term.current_term()).get(trainee=self.request.user.trainee)
        context['roll'] = Roll.objects.filter(trainee=self.request.user.trainee).filter(timestamp__gte=Term.current_term().start)
        return context
