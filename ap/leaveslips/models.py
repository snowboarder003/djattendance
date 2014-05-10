from django.db import models

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

    class Meta:
        abstract = True


class IndividualSlip(models.Model):


class GroupSlip(models.Model):


class MealOutSlip(models.Model):


class NightOutSlip(models.Model):
