from django.db import models
from django.contrib.auth.models import Group
	

#Define Service Category such as Cleaning, Guard, etc.
class Category(Group):
    """
    Defines a service category such as Clean-up, Guard, Mopping, Chairs, etc.
    """

    description = models.TextField()

    def __unicode__(self):
        return self.name


#define Service such as Breakfast Cleaning, Dinner Prep, Guard A, etc
class Service(Group):
    """" 
	FTTA service class to define service such as
    Breakfast Clean-up, Dinner Prep, Guard A, Wednesday Chairs, etc.
    This also includes designated services such as Accounting or Lights.
    """

    category = models.ForeignKey(Category, related_name="services")
    isActive = models.BooleanField()

    #Every service has different workload to describe its 
	#service hours and service intensity
    workload = models.IntegerField()
	
	#whether this service needs certain qualified trainees
    needQualification = models.BooleanField(blank=True)

	#Service qualification such as Sack lunch star,Kitchen Star,
	#Shuttle Driver, Piano, Usher, etc
    #Note: This is different from permanent designation. For example, 
	#two brothers are be designated as AV brothers,
    #but others brothers have the qualification to serve AV.
	qualifiedTrainees = models.ManyToManyField('accounts.Trainee')

    def __unicode__(self):
        return self.name


#Define Service Period such as Pre-Training, FTTA regular week, etc
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
