from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from aputils.models import Vehicle, Address
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

""" accounts models.py
The user accounts module takes care of user accounts for the attendance+

There are several different kinds of users
    - Trainee:
    - TrainingAssistant
    - ShortTermTrainee
    - HospitalityGuest
"""


class EmergencyInfo(models.Model):

    name = models.CharField(max_length=30)

    address = models.ForeignKey(Address)

    #contact's relation to the trainee.
    relation = models.CharField(max_length=30)

    phone = models.CharField(max_length=15)

    phone2 = models.CharField(max_length=15)


class UserAccount(AbstractUser):

    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    #optional middle name. First and last are in the abstract
    middleName = models.CharField(max_length=30, blank=True)

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
        except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
            birthday = birth.replace(year=today.year, day=birth.day-1)
        if birthday > today:
            return today.year - birth - 1
        else:
            return today.year - birth

    age = property(get_age)

    maritalStatus = models.BooleanField()


class TrainingAssistant(UserAccount):

    user = models.ForeignKey(UserAccount)


class Trainee(UserAccount):

    user = models.ForeignKey(UserAccount)

    term = models.ManyToManyField(Term)

    type = models.CharField(max_length=30)

    spouse = models.OneToOneField('self')

    emergencyInfo = models.OneToOneField(EmergencyInfo)

    dateBegin = models.DateField()

    dateEnd = models.DateField()

    degree = models.CharField(max_length=30)

    mentor = models.ForeignKey('self')

    vehicle = models.ForeignKey(Vehicle)

    schedule = models.ForeignKey("Schedule")

    team = models.ForeignKey(Team)

    services = models.ManyToManyField(Service)

 #   gospelPreferences = models.CharField()

    house = models.ForeignKey(House)

    TA = models.ForeignKey(TrainingAssistant)

    bunkNumber = models.ForeignKey(Bunk)

    #boolean for if the trainee is active in the training or not.
    active = models.BooleanField()

    #flag for trainees being self attended. This will be false for 1st years and true for 2nd with some exceptions.
    selfAttendance = models.BooleanField()


class ShortTermTrainee(UserAccount):

    user = models.ForeignKey(UserAccount)

    #date that they begin to be assigned to service
    serviceDate = models.DateField()

    #date that they leave the training. No service should be assigned after this point
    departureDate = models.DateField()


class HospitalityGuest(UserAccount):

    user = models.ForeignKey(UserAccount)

    #date that they leave the training. No service should be assigned after this point
    departureDate = models.DateField()
