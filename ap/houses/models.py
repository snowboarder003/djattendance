from django.db import models
from utils.models import Address

""" HOUSES models.py

This houses module is a utility model that define training housing.

Data Models:
- House: a training house

- Bunk: a bunk (either lower of upper) in a given house

"""


class House(models.Model):

    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    # the common name for the house, e.g. 1329 Amberwick, 2102 Grace
    name = models.CharField(max_length=50)

    # the house's address (defined in the utils class)
    address = ForeignKey(Address)

    # whether this is a brother's house or a sister's house
    gender = models.CharField(max_length=1, choices=GENDER)

    # whether this house is actively used by the training
    used = models.BooleanField()

    def __unicode__(self):
        return self.name


class Room(models.Model):

    capacity = models.SmallIntegerField()

    house = models.ForeignKey(House)

    floor = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.house.name + " Room " + self.pk


class Bunk(models.Model):

    POSITION = (
        ('T', 'Top'),
        ('B', 'Bottom')
    )

    # the bunk's number
    number = models.SmallIntegerField(primary_key=True)

    # whether this is a top or bottom bunk
    position = models.CharField(max_length=1, choices=POSITION)

    # which room this bunk is in
    room = models.ForeignKey(Room)

    # which trainee is in this bunk
    trainee = models.OneToOneField('Trainee')

    def __unicode__(self):
        return self.room.house.name + " Bunk " + self.number
