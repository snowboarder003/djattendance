from django.http import HttpResponse
from disciplines.models import Discipline, Summary

def discipline(request):
    latest_summaries = Discipline.objects.order_by('offense')
    output = ', '.join(["Life-Study Summary due as " + d.offense + " for " + d.infraction + " infraction ; " for d in latest_summaries])
    return HttpResponse(output)

def write(request):
    response = "Life-Study Summary"
    return HttpResponse(response)

def result(request):
    return HttpResponse("Your life-study summary has been successfully submitted.")
