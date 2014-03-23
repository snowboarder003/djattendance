from datetime import date

from django.db import models

from terms.models import Term
from classes.models import Class
from accounts.models import Trainee


""" SCHEDULES models.py

This schedules module is for representing weekly trainee schedules.

Data Models
- Event:
    an event, such as class or study time, that trainees need to attend.
- EventGroup:

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
        ('H', 'House'),
        ('T', 'Team'),
        ('L', 'Church Meeting'),  # C is taken, so L for locality
        ('*', 'Special'),  # S is taken, so * for special
    )

    MONITOR_TYPES = (
        ('AM', 'Attendance Monitor'),
        ('TM', 'Team Monitor'),
        ('HC', 'House Coordinator'),
    )

    # name of event, e.g. Full Ministry of Christ, or Lights Out
    name = models.CharField(max_length=30)

    # the event's shortcode, e.g. FMoC or Lights
    code = models.CharField(max_length=10)

    # a description of the event (optional)
    description = models.CharField(max_length=250, blank=True)

    # a groupID. used to group repeating events
    group = models.ForeignKey('EventGroup', blank=True, null=True)

    # if this event is a class, relate it
    classs = models.ForeignKey(Class, blank=True, null=True)  # class is a reserved keyword :(

    # the type of event
    type = models.CharField(max_length=1, choices=EVENT_TYPES)

    # who takes roll for this event
    monitor = models.CharField(max_length=2, choices=MONITOR_TYPES, blank=True, null=True)

    # which term this event is active in
    term = models.ForeignKey(Term)

    date = models.DateField()

    start = models.TimeField()

    end = models.TimeField()

    def _week(self):
        self.term.reverseDate(self.date)[0]
    week = property(_week)
    
    def _day(self):
        self.term.reverseDate(self.date)[1]
    day = property(_day)


class EventGroup(models.Model):

    # for now, this should just be the same as the event name
    name = models.CharField(max_length=30)

    # which days this event repeats, starting with Monday (0) through LD (6)
    # i.e. an event that repeats on Tuesday and Thursday would be (1,3)
    repeat = models.CommaSeparatedIntegerField(max_length=7)

    # override delete(): ensure all events in eventgroup are also deleted
    def delete(self, *args, **kwargs):
        Events.objects.filter(eventgroup=self.id).delete()
        super(EventGroup, self).delete(*args, **kwargs)


class Schedule(models.Model):

    # which trainee this schedule belongs to
    trainee = models.ForeignKey(Trainee)

    # which term this schedule applies to
    term = models.ForeignKey(Term)

    # which events are on this schedule
    events = models.ManyToManyField(Event, null=True, blank=True)

    def todays_events(self):
        return self.events.filter(date__exact=date.today())

    class Meta:
        # a trainee should only have one schedule per term
        unique_together = (('trainee', 'term'))


class ScheduleTemplate(models.Model):

    name = models.CharField(max_length=20)

    eventgroup = models.ManyToManyField(EventGroup)  # TODO: consider refactor using postgres arrays
    
    def apply(schedule, self):
        """ applies a schedule template to a schedule """
        for eventgrp in EventGroup.objects.filter(scheduletemplate=self.id):
            # iterate over each event inside each event group
            for event in Event.objects.filter(eventgroup=eventgrp.id):
                schedule.events.add(event)

    def apply_multiple(schedules, self):
        """ applies a schedule template to a group of schedules """
        for schedule in schedules:
            self.apply(schedule)
