from django.db import models

""" ROOMS models.py

The ROOMS app represents rooms that are in the Training Center (TC). This is
used by other apps such as Room Reservation and Maintenance Requests.

Data Models:
    - Room: a room inside the TC
"""


class Room (models.Model):

    ROOM_TYPES = (
        ('Cr', 'Classroom'),
        ('FR', 'Fellowship Room'),
        ('SR', 'Study Room'),
        ('CA', 'Common Area'),
        ('Cf', 'Cafeteria'),
    )

    ACCESS_TYPES = (
        ('C', 'Common'),
        ('B', 'Brothers'),
        ('S', 'Sisters'),
        ('R', 'Restricted'),
    )

    # the room's number
    number = models.SmallIntegerField(primary_key=True)

    # the abbreviated name
    shortcode = models.CharField(max_length=20)

    # which floor of the TC this room is on
    floor = models.SmallIntegerField()

    # not sure if this is needed
    type = models.CharField(max_length=2, choices=ROOM_TYPES, blank=True)

    # the access of this room, e.g. brothers only, sisters only,
    access = models.CharField(max_length=1, choices=ACCESS_TYPES)

    # some rooms are in the system and have schedules, but cannot be reserved
    reservable = models.BooleanField()
