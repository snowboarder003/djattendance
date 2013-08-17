from django.db import models
from schedules.models import Event
from accounts.models import Trainee
from terms.models import Term

""" attendance models.py
The attendance module takes care of data and logic directly related
to tracking attendance. It does not handle things such as schedules
or leave slips.

DATA MODELS:
    - Roll: an attendance record per trainee, per event.
            for example, if 10 trainees are supposed to be at an event,
            then there will be 10 roll objects associated to that event,
            as well as each trainee.

    - Period: a set of attendance records, generally a 2-week period
"""


class Roll(models.Model):

    ROLL_STATUS = (
        ('A', 'Absent'),
        ('T', 'Tardy'),
        ('U', 'Uniform'),
        ('L', 'Left Class'),
        ('P', 'Present')
    )

    event = models.ForeignKey(Event)

    trainee = models.ForeignKey(Trainee)

    status = models.CharField(max_length=1, choices=ROLL_STATUS)

    # once a roll is finalized, it can no longer be edited
    # except by a TA, attendance monitor, or other admin
    finalized = models.BooleanField(default=False)

    notes = models.CharField(max_length=200, blank=True)

    # the one who submitted this roll
    monitor = models.ForeignKey(Trainee, blank=True)

    timestamp = models.DateTimeField(auto_now=True)


class Period(models.Model):

    # the beginning week of this period
    start = models.SmallIntegerField()

    # the ending week of this period
    end = models.SmallIntegerField()

    term = models.ForeignKey(Term)
