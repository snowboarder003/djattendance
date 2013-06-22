from django.db import models


class serviceCategory(models.Model):
    Name = models.CharField(max_length=200)
    description = models.TextField()

class service(models.Model):
    category = models.ForeignKey(serviceCategory)
    serviceName = models.CharField(max_length=1000)
    isActive = models.BooleanField()
    workLord = models.IntegerField()

class servicePeriod(models.Model):
    periodName = models.CharField(max_length=200)
    service = models.ManyToManyField(service) #which services is on this Period
    startDate = models.DateField('start date')
    endDate = models.DateField('end date')
    
class serviceInstance(models.Model):
    
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
    period = models.ForeignKey(servicePeriod)
    weekday = models.CharField(max_length=3, choices=WEEKDAY)
    startTime = models.TimeField('start time')
    endTime = models.TimeField('end time')
    recoveryTime = models.IntegerField('time')
