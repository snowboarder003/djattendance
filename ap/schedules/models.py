from django.db import models

########################################################################80chars

""" SCHEDULES models.py

This schedules module is for representing weekly trainee schedules.

Data Models
- Event: 
    an event, such as class or study time, that trainees need to attend.
- Schedule: 
    a collection of events for one trainee. each trainee should have one 
    schedule per term. 
- ScheduleTemplate:
    a generic collection of events for one week that can be applied to a 
    trainee or group of trainees. 

"""

class Event(models.Model):

    EVENT_TYPES = (
        ('C', 'Class'),
        ('S', 'Study'),
        ('M', 'Meal'),
        ('H','House'),
        ('T','Team'),
        ('L','Church Meeting'), # C is taken, so L for locality
        ('*', 'Special'), # S is taken, so * for special
    )

    MONITOR_TYPES = (
        ('AM', 'Attendance Monitor'),
        ('TM', 'Team Monitor'),
        ('HC', 'House Coordinator'),
    )

    # name of event, e.g. Full Ministry of Christ, or Lights Out
    name = models.CharField(max_length=30)

    # the event's shortcode, e.g. FMoC or Lights
    shortcode = models.CharField(max_length=10)

    # a description of the event (optional)
    description = models.CharField(max_length=250, blank=True)

    # a groupID. used to group repeating events
    group = models.IntegerField()

    # the type of event
    type = models.CharField(max_length=1, choice=EVENT_TYPES)

    # who takes roll for this event
    monitor = models.CharField(max_length=2, choice=MONITOR_TYPES)

    # which term this event is active in
    'term = models.ForeignKey()  # TODO: write and import TERM

    # which days this event repeats on, starting with Monday (0) through LD (6)
    # an event that repeats on Tuesday and Thursday would be (1,3)
    repeat = models.CommaSeparatedIntegerField(max_length=7)

    # weeks 0-19 for the 20 weeks of the training
    week = models.PositiveSmallIntegerField()

    # days 0-6 (LD through Saturday)
    day = models.PositiveSmallIntegerField()

    start = models.TimeField()

    end = models.TimeField()

class Schedule(models.Model):

    # which trainee this schedule belongs to
    'trainee = models.ForeignKey() #TODO: write and import user model

    # which term this schedule applies to
    term = models.ForeignKey() #TODO: write and import TERM

    # which events are on this schedule
    events = models.ManyToManyField(Event)

class ScheduleTemplate(models.Model):

