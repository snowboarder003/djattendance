from django.db import models
#from users.models import UserAccount

#This is for define service


#define service category such as Cleaning, Guard etc
class category(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    #return services of this category
    def getService(self):
        return service.objects.filter(category=self)


#define service such as Breakfast Cleaning, Dinner Prep, Guard A, etc
class service(models.Model):

    category = models.ForeignKey(category)
    name = models.CharField(max_length=1000)
    isActive = models.BooleanField()
    workLoad = models.IntegerField()


#define service Period such as Pre-Training, FTTA regular week, etc
class period(models.Model):

    name = models.CharField(max_length=200)

    #which service is on this Period
    service = models.ManyToManyField(service)

    startDate = models.DateField('start date')
    endDate = models.DateField('end date')

    #return the services of this Period
    def getService(self):
        return service.objects.filter(period=self)


#define one specific service instance such as Monday Break Prep, Monday Guard C, etc
class instance(models.Model):

    WEEKDAY = (
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    )

    service = models.ForeignKey(service)
    period = models.ForeignKey(period)
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    startTime = models.TimeField('start time')
    endTime = models.TimeField('end time')
    recoveryTime = models.IntegerField('time')

