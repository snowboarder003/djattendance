from django.db import models
from django.contrib.auth.models import Group


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

class Category(Group):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """

    description = models.TextField()

    def __unicode__(self):
        return self.name


class Service(Group):
    """" 
	FTTA service class to define service such as
    Breakfast Clean-up, Dinner Prep, Guard A, Wednesday Chairs, etc.
    This also includes designated services such as Accounting or Lights.
    """

    category = models.ForeignKey(Category, related_name="services")
    active = models.BooleanField()

    #Every service has different workload to describe its service hours and service intensity
    workload = models.IntegerField()
	
	#whether this service needs certain qualified trainees
    needQualification = models.BooleanField(blank=True)

	#Service qualification such as Sack lunch star,Kitchen Star,
	#Shuttle Driver, Piano, Usher, etc
    #Note: This is different from permanent designation. For example, 
	#two brothers are be designated as AV brothers,
    #but others brothers have the qualification to serve AV.
	qualifiedTrainees = models.ManyToManyField('accounts.Trainee')

    #whether this service needs certain qualified trainees
    need_qualification = models.BooleanField(blank=True)

    #Service qualification such as Sack lunch star,Kitchen Star,
    #Shuttle Driver, Piano, Usher, etc
    #Note: This is different from permanent designation. For example,
    #two brothers are be designated as AV brothers,
    #but others brothers have the qualification to serve AV.
    qualifiedTrainees = models.ManyToManyField('accounts.Trainee', blank=True)

    def __unicode__(self):
        return self.name


class Period(models.Model):
    """Define Service Period such as Pre-Training, FTTA regular week, etc"""

    name = models.CharField(max_length=200)
    description = models.TextField()

    #Service which is in this Period
    service = models.ManyToManyField(Service, related_name="periods")

    startDate = models.DateField('start date')
    endDate = models.DateField('end date')

    def __unicode__(self):
        return self.name
