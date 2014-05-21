from django.http import HttpResponse
from lifestudies.models import LifeStudy, Summary

def lifestudy(request):
    latest_summaries = LifeStudy.objects.order_by('offense')
    output = ', '.join(["Life-Study Summary due as " + d.offense + " for " + d.infraction + " infraction ; " for d in latest_summaries])
    return HttpResponse(output)

def write(request):
    response = "Life-Study Summary"
    return HttpResponse(response)

def result(request):
    return HttpResponse("Your life-study summary has been successfully submitted.")
