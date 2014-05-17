from django.db import models

from schedules.models import Event
from accounts.models import Trainee, TrainingAssistant


""" leaveslips models.py
The leavelslip module takes care of all logic related to... you guessed it, leave slips.


DATA MODELS:
    - LeaveSlip: an abstract class that contains information common to all leave
    leave slips. Extended by Individual and Group slips.

    - IndividualSlip: extends LeaveSlip generic class. A leave slip that only
    applies to one trainee (but can apply to multiple events)

    - GroupSlip: extends LeaveSlip generic class. A leaveslip that can apply to
    a group of trainees, and covers a time range (rather than certain events).

    - MealOutSlip: an extension to a leaveslip, containing information relevant
    to a pre-excused meal out.

    - NightOutSlip: an extension to a leaveslip, containing information relevant
    to a pre-excused night out.
"""


class LeaveSlip(models.Model):

    LS_TYPES = (
        ('CONF', 'Conference'),
        ('EMERG', 'Family Emergency'),
        ('FWSHP', 'Fellowship'),
        ('FUNRL', 'Funeral'),
        ('GOSP', 'Gospel'),
        ('INTVW', 'Grad School/Job Interview'),
        ('GRAD', 'Graduation'),
        ('MEAL', 'Meal Out'),
        ('NIGHT', 'Night Out'),
        ('OTHER', 'Other'),
        ('SERV', 'Service'),
        ('SICK', 'Sickness'),
        ('SPECL', 'Special'),
        ('WED', 'Wedding'),
        ('NOTIF', 'Notification Only'),
    )

    LS_STATUS = (
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('F', 'Fellowship'),
        ('D', 'Denied'),
        ('S', 'TA sister approved'),
    )

    #add id as primary key
    #add assigned to TA

    type = models.CharField(max_length=5, choices=LS_TYPES)
    status = models.CharField(max_length=1, choices=LS_STATUS)

    TA = models.ForeignKey(TrainingAssistant)
    
    submitted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    finalized = models.DateTimeField(blank=True, null=True)  # when this leave-slip was approved/denied

    description = models.TextField(blank=True, null=True)  # trainee-supplied
    comments = models.TextField(blank=True, null=True)  # for TA comments

    texted = models.BooleanField(default=False)  # for sisters only

    informed = models.BooleanField(blank=True, default=False)  # not sure, need to ask

    def _late(self):
        pass  # TODO

    late = property(_late)  # whether this leave slip was submitted late or not

    class Meta:
        abstract = True


class IndividualSlip(LeaveSlip):

    events = models.ManyToManyField(Event)
    trainee = models.ForeignKey(Trainee)


class GroupSlip(LeaveSlip):

    start = models.DateTimeField()
    end = models.DateTimeField()
    trainee = models.ManyToManyField(Trainee)


class MealOutSlip(models.Model):

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class NightOutSlip(models.Model):

    hostname = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    hostaddress = models.CharField(max_length=255)
    HC = models.ForeignKey(Trainee)
