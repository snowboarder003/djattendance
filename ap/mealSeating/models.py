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

    def getSeatedTrainees(self):
        return self.seatedTrainees.all()

    def getCapacity(self):
        return self.capacity

    def __unicode__(self):
        return self.name
    
    @staticmethod
    def seatBrothers(traineeList):
        tables = list(Table.objects.filter(genderType="B"))

        tableToAddTo = 0

        for trainee in traineeList:
            if not tables[tableToAddTo].isFull():
                tables[tableToAddTo].seatTrainee(trainee)
            else:
                if(tableToAddTo < len(tables)):
                    tableToAddTo +=1
                    tables[tableToAddTo].seatTrainee(trainee)
    