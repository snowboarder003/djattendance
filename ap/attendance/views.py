from itertools import chain

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404

from .models import Roll, Period
from schedules.models import Schedule, Event
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import User
from leaveslips.models import IndividualSlip, IndividualSlipForm


class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(AttendancePersonal, self).get_context_data(**kwargs)
        context['trainee'] = self.request.user.trainee
        context['schedule'] = Schedule.objects.filter(term=Term.current_term()).get(trainee=self.request.user.trainee)
        context['attendance'] = Roll.objects.filter(trainee=self.request.user.trainee).filter(event__term=Term.current_term())
<<<<<<< HEAD
        context['leaveslipform'] = IndividualSlipForm()
=======
        context['leaveslips'] = chain(list(IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())), list(GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)))
>>>>>>> 91446b92349625bc271a19f8302f8b6dec763594
        return context
