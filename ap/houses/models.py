from django.db import models

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

    # the actual mailing address of the house
    address = models.CharField(max_length=200)

    # whether this is a brother's house or a sister's house
    gender = models.CharField(max_length=1, choices=GENDER)

    # whether this house is actively used by the training
    used = models.BooleanField()


class Room(models.Model):

    capacity = models.SmallIntegerField()

    house = models.ForeignKey(House)

    floor = models.SmallIntegerField(default=1)


class Bunk(models.Model):

    POSITION = (
        ('T', 'Top'),
        ('B', 'Bottom')
    )

    # the bunk's number
    number = models.SmallIntegerField()

    # whether this is a top or bottom bunk
    position = models.CharField(max_length=1, choices=POSITION)

    # which room this bunk is in
    room = models.ForeignKey(Room)

    # which trainee is in this bunk
    trainee = models.OneToOneField('Trainee')
