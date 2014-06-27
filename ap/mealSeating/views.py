from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from mealSeating.models import Table
from accounts.models import User


@csrf_protect
def seattables(request):
    filterchoice = request.POST['Filter']
    genderchoice = request.POST['Gender']

    trainees = User.objects.all().filter(is_active=1, gender=genderchoice).order_by(filterchoice)[:50]

    mydict = Table.seatinglist(trainees,genderchoice)

    return render(request, 'detail.html', {'mydict' : mydict})

def newseats(request):
    return render(request, 'newSeating.html')

def signin(request):
    trainees = User.objects.all().filter(is_active=1).values("lastname","firstname").order_by("lastname")[:50]
    return render(request, 'mealsignin.html', {'trainees' : trainees})