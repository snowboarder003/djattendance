from django.http import HttpResponse
from lifestudies.models import LifeStudy, Summary
from django.views.generic import ListView

class LifeStudyListView(ListView):
    template_name = 'lifestudies/lifestudylist.html'
    model = LifeStudy
    context_object_name = 'lifestudies'

    def get_context_data(self, **kwargs):
        context = super(LifeStudyListView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context

# def lifestudy(request):
#     latest_summaries = LifeStudy.objects.order_by('offense')
#     output = ', '.join(["Life-Study Summary due as " + d.offense + " for " + d.infraction + " infraction ; " for d in latest_summaries])
#     return HttpResponse(output)

# def write(request):
#     response = "Life-Study Summary"
#     return HttpResponse(response)

# def result(request):
#     return HttpResponse("Your life-study summary has been successfully submitted.")
