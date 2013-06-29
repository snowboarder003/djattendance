from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from utilities.models import Vehicle, Address
from term_stub.models import Term
from teams_stub.models import Teams
from houses_stub.models import house


class UserAccount(AbstractUser):
    
     GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    #optional middle name. First and last are in the abstract
    middleName = models.CharField(max_length=30)
    
    nickname = models.CharField(max_length=30)
    
    maidenName = models.CharField(max_length=30)
    
    birthdate = models.DateField() 
    
    gender = models.CharField(max_length=1, choices=GENDER)
    
    address = models.ForeignKey(Address)
    
    #return the age based on birthday
    def get_age(self):
        today = date.today()
        birth = date.fromtimestamp(self.birthdate)
        try: 
            birthday = birth.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = birth.replace(year=today.year, day=birth.day-1)
        if birthday > today:
            return today.year - birth - 1
        else:
            return today.year - birth

    age = property(get_age)
    
    maritalStatus = models.BooleanField()

     
class TraineeAccount(UserAccount):
    
    user = models.ForeignKey(UserAccount)
    
    term = models.ManyToManyField(Term)
    
    type = models.CharField(max_length = 30)
    
    spouse = models.ForeignKey("TraineeAccount")
    
    emergencyInfo = models.ForeignKey("emergencyInfo")
    
    dateBegin = models.DateField()
    
    dateEnd = models.DateField()
    
    degree = models.CharField(max_length=30)
    
    mentor = models.ForeignKey("TraineeAccount")
    
    vehicle = models.ForeignKey(Vehicle)
    
    schedule = models.ForeignKey(ss.schedule)
    
    team = models.ForeignKey(Teams)
    
    services = models.ManyToManyField(services.services)
    
    gospelPreferences = models.CharField()
    
    house = models.ForeignKey(House)
    
    TA = models.ForeignKey("TrainingAssistantAccount")
    
    bunkNumber = models.ForeignKey(house.bunk)
    
    #boolean for if the trainee is active in the training or not.
    active = models.BooleanField()
    
    #flag for trainees being self attended. This will be false for 1st years and true for 2nd with some exceptions.
    selfAttended = models.BooleanField()


class TrainingAssistantAccount(UserAccount):
    
    user = models.OneToOneField(UserAccount.user)
    
    maritalStatus = models.BooleanField
    

class ShortTermTrainee(UserAccount):
    
    user = models.OneToOneField(UserAccount.user)
    
    #date that they begin to be assigned to service
    serviceDate = models.DateField()
    
    #date that they leave the training. No service should be assigned after this point
    departureDate = models.DateField()


class HospitalityGuest(UserAccount):
    
    user = models.OneToOneField(UserAccount.user)
    
    #date that they leave the training. No service should be assigned after this point
    departureDate = models.DateField()


class EmergencyInfo(Model.models):
    
    name = models.CharField(max_length=30)
    
    address= models.foreignkey(Address)
    
    #contact's relation to the trainee.
    relation = models.CharField(max_length=30)
    
    phone = models.CharField(max_length=15)
    
    phone2 = models.CharField(max_length=15)