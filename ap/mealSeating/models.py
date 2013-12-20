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
    seatedTrainees = models.ManyToManyField(Trainee)
    location = models.CharField(max_length=2, choices=LOCATIONS)

    def getEmptySeats(self):
        return self.capacity - self.seatedTrainees.count()

    def getSeatedTrainees(self):
        return self.seatedTrainees.all()

    def getCapacity(self):
        return self.capacity

    def __unicode__(self):
        return self.name
