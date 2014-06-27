# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from django_tables2 import RequestConfig
from django_tables2 import tables

from mealSeating.models import Table
#from .tables import TablesTable

from accounts.models import User, Trainee, Profile

# def seating(request):
#     return HttpResponse("Hello, world. You're at the meal seating page.")

@csrf_protect
def seattables(request):
    filterchoice = request.POST['Filter']
    genderchoice = request.POST['Gender']

    trainees = User.objects.all().filter(gender=genderchoice).order_by(filterchoice)[:50]
    tablesList = Table.objects.all()

    mydict = Table.seatinglist(trainees,genderchoice)

    return render(request, 'detail.html', {'mydict' : mydict})

def newseats(request):
    return render(request, 'newSeating.html')

# def brothertables(request):

#     trainees = Trainee.objects.all().filter(account__gender__contains="B").order_by('account__firstname')[:50]
#     tablesList = Table.objects.all()

#     myList = Table.seatTables(trainees, tablesList)

#     splitValue = len(myList) / 3

#     myList1 = myList[:splitValue]
#     myList2 = myList[splitValue:splitValue*2]
#     myList3 = myList[splitValue*2:]

#     return render(request, 'detail.html', {'myList1': myList1 , 'myList2': myList2, 'myList3' : myList3})


# def sistertables(request):

#     trainees = Trainee.objects.all().filter(account__gender__contains="S").order_by('account__firstname')[:50]
#     tablesList = Table.objects.all()

#     myList = Table.seatTables(trainees, tablesList)


#     splitValue = len(myList) / 3

#     myList1 = myList[:splitValue]
#     myList2 = myList[splitValue:splitValue*2]
#     myList3 = myList[splitValue*2:]

#     return render(request, 'detail.html', {'myList1': myList1 , 'myList2': myList2, 'myList3' : myList3})


# class ViewList(ListView):
#     model = Table
#     context_object_name = 'table'