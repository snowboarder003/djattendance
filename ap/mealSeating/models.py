from django.db import models

from accounts.models import Trainee

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

    seatedTrainees = models.ManyToManyField(Trainee)
    location = models.CharField(max_length=2, choices=LOCATIONS)
    genderType = models.CharField(max_length=1, choices=GENDERS)


    def getEmptySeats(self):
        return self.capacity - self.seatedTrainees.count()

    def isFull(self):
        return self.getEmptySeats() == 0

    def seatTrainee(self, trainee):
        if(self.getEmptySeats() != 0):
            self.seatedTrainees.add(trainee)
            return True
        else:
            return False

    def splitTablesByGender(self, tables):
        brothersTables = []
        sistersTables = []
        tableSplit = [brothersTables, sistersTables]

        for table in tables:
            if table.genderType == "B":
                brothersTables.append(table)
            else:
                sistersTables.append(table)

        return tableSplit

    def getSeatedTrainees(self):
        return self.seatedTrainees.all()

    def getCapacity(self):
        return self.capacity

    def __unicode__(self):
        return self.name
    
    @staticmethod
    def seatTables(traineeList, tableList):
        tables = Table().splitTablesByGender(tableList)
        tableToAddTo = 0
        seatingList = []
        brothers = 0
        sisters = 1

        for trainee in traineeList:
            if trainee.account.gender == "B":
                gender = brothers
            else:
                gender = sisters

            if tables[gender][tableToAddTo].isFull() & (tableToAddTo < len(tables[gender])):
                tableToAddTo +=1
            tables[gender][tableToAddTo].seatTrainee(trainee)
            seatingList.append([trainee.account.get_full_name(),tables[gender][tableToAddTo].name])

        return seatingList