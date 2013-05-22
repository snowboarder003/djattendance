from django.db import models

########################################################################80chars

"""
SCHEDULES models.py

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
    group = models.IntegerField(unique=True)
    

class Schedule(models.Model):

class ScheduleTemplate(models.Model):

