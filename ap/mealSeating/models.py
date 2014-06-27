from django.db import models

""" mealSeating models.py

This module prints the bi-weekly meal seating list for the FTTA and FTTMA
brothers and sisters, and also for short-termers.
"""

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

    location = models.CharField(max_length=2, choices=LOCATIONS)
    genderType = models.CharField(max_length=1, choices=GENDERS)

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
            print "cannot seat " + traineenum + " trainees. Current capacity is: " + totalcapacity
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