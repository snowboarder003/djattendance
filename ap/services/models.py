from django.db import models
from django.contrib.auth.models import Group

from ss.models import Qualification

""" services models.py

The services model defines both weekly and permanent (designated) services in the

Data Models:
    - Category: This is a broad category that contains specific services. For
    example,Cleanup is a category that contains services such as Tuesday
    Breakfast Cleanup or Saturday Lunch Cleanup. Guard contains Guards A, B, C,
    and D.

    - Service: This refers to a specific service that repeats on a weekly basis.
    I.e. Tuesday Breakfast Prep is a service. It repeats every week. A specific
    instance of that service is defined in the service scheduler module as a
    service Instance.

    - Period: This is a period in which services are active and generally
    changes with the schedule of the training. Most of the time, the regular
    FTTA schedule will be in effect, but there are exceptions such as Service
    Week and the semiannual training.
"""

class Category(models.Model):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Period(models.Model):
    """
    Defines a service period such as Pre-Training, FTTA regular week, etc
    """

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Service(Group):
    """
	Defines a weekly service, whether rotational (e.g. Tuesday Breakfast Clean-up)
    or designated (e.g. Attendance Project, Vehicle Maintenance, or Lights)
    """

    WEEKDAYS = (
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
    )

    category = models.ForeignKey(Category, related_name="services")
    period = models.ManyToManyField(Period)

    active = models.BooleanField(default=True)
    designated = models.BooleanField()

    # on a scale of 1-12, with 12 being the most intense
    workload = models.IntegerField()
    recovery_time = models.PositiveSmallIntegerField()  # in hours

    qualifications = models.ManyToManyField(Qualilfication)

    weekday = models.CharField(max_length=3, choices=WEEKDAYS)
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return self.name
