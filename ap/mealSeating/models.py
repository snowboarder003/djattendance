from django.db import models

from accounts.models import Trainee

""" mealSeating models.py

This module prints the bi-weekly meal seating list for the FTTA and FTTMA
brothers and sisters, and also for short-termers.
"""



#dict ((o.lastname + ", " + o.firstname, o.pk) for o in User.objecs.all())
# 
#
# for o in sortedList:
#   mydict[o.account.lastname + ", " + o.account.firstname] = o.pk
#
# <ul>
# {% for key, value in choices.items %} 
#   <li>{{key}} - {{value}}</li>
#  {% endfor %}
# </ul>

# def seatinglist(genderlist, gender):
#     tables = Table.objects.filter(genderType = gender)
#     traineenum = 1
#     tablenum = 0
#     mealSeating = {}
#     totalcapacity = 0
#     for x in Table.objects.all().filter(genderType = gender).values("capacity"):
#         totalcapacity += x["capacity"]
    # if (len(genderlist) > totalcapacity):
#         print "cannot seat " + traineenum + " trainees. Current capacity is: " + capacity
    # else:
    #     for trainee in genderlist:    
    #         if ( traineenum == tables[tablenum].capacity):
    #             tablenum += 1
    #             traineenum = 0
    #         mealseating[trainee.lastname + ", " + trainee.firstname] = tables[tablenum]
    #         traineenum += 1
    #     return mealSeating    

class Table(models.Model):

    name = models.CharField(max_length=10)
    capacity = models.IntegerField(null=True)
    LOCATIONS = (
        ('W', 'West Cafeteria'),
        ('M', 'Main Cafeteria'),
        ('S', 'South Cafeteria'),
        ('SE', 'Southeast Cafeteria'),
    )
    GENDERS = (
        ('B', 'Brother'),
        ('S', 'Sister'),
    )

    # seatedTrainees = models.ManyToManyField(Trainee, blank=True, null=True)
    location = models.CharField(max_length=2, choices=LOCATIONS)
    genderType = models.CharField(max_length=1, choices=GENDERS)


    # def getEmptySeats(self):
    #     return self.capacity - self.seatedTrainees.count()

    # def isFull(self):
    #     return self.getEmptySeats() == 0

    # def clearTables(self):
    #     self.seatedTrainees = []
    #     return True

    # def seatTrainee(self, trainee):
    #     if(self.getEmptySeats() != 0):
    #         self.seatedTrainees.add(trainee)
    #         return True
    #     else:
    #         return False

    # def clearTrainees(self):
    #     for tables in Table.objects.all():
    #         tables.seatedTrainees.clear()
    #     return True

    # def splitTablesByGender(self, tables):
    #     brothersTables = []
    #     sistersTables = []
    #     tableSplit = [brothersTables, sistersTables]

    #     for table in tables:
    #         if table.genderType == "B":
    #             brothersTables.append(table)
    #         else:
    #             sistersTables.append(table)

    #     return tableSplit

    # def getSeatedTrainees(self):
    #     return self.seatedTrainees.all()

    def getCapacity(self):
        return self.capacity

    def __unicode__(self):
        return self.name
    
    @staticmethod
    def seatinglist(genderlist, gender):
        tables = Table.objects.filter(genderType = gender)
        traineenum = 0
        tablenum = 0
        totalcapacity = 0
        meal_list = []
        for x in Table.objects.all().filter(genderType = gender).values("capacity"):
            totalcapacity += x["capacity"]
        if (len(genderlist) > totalcapacity):
            print "cannot seat " + traineenum + " trainees. Current capacity is: " + capacity
        else:
            for trainee in genderlist:    
                mealseating = {}
                if ( traineenum == tables[tablenum].capacity):
                    tablenum += 1
                    traineenum = 0
                mealseating["first_name"] = trainee.firstname
                mealseating["last_name"] = trainee.lastname
                mealseating["table"] = tables[tablenum]
                meal_list.append(mealseating)
                traineenum += 1
            return meal_list    

    # @staticmethod
    # def seatTables(traineeList, tableList):
    #     tables = Table().splitTablesByGender(tableList)

    #     Table().clearTrainees()

    #     tableToAddTo = 0
    #     seatingList = []
    #     brothers = 0
    #     sisters = 1
    #     broCounter = 0
    #     sisCounter = 0
    #     firstPass = True

    #     for trainee in traineeList:
    #         if trainee.account.gender == "B":
    #             gender = brothers
    #             tableToAddTo = broCounter
    #         else:
    #             gender = sisters 
    #             tableToAddTo = sisCounter

    #         if(firstPass is False):
    #             if tables[gender][tableToAddTo].isFull() & (tableToAddTo <= (len(tables[gender])-1)):
    #                 if trainee.account.gender == "B":
    #                     broCounter += 1
    #                     tableToAddTo = broCounter
    #                 else:
    #                     sisCounter += 1
    #                     tableToAddTo = sisCounter
    #                 firstPass = True

    #         tables[gender][tableToAddTo].seatTrainee(trainee)
    #         entry = []
    #         entry.append([trainee.account.get_full_name(),tables[gender][tableToAddTo].name])
    #         seatingList.append(entry)
    #         firstPass = False

    #     return seatingList