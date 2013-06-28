from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from utilities.models import Vehicle, Address
from term_stub.models import Term
from teams_stub.models import Teams
from houses_stub.models import house

# UserAccounts is the abstract class for all accounts.
class UserAccount(AbstractUser):
    middleName = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    maidenName = models.CharField(max_length=30)
    birthdate = models.DateField() 
    gender = models.CharField(max_length = 10) 
    address = models.ForeignKey(Address)
    def get_age(self):
        "returns the age"
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

#TraineeAccount is the model for all trainees.        
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

#TrainingAssistantAccount is the account type for TAs
class TrainingAssistantAccount(UserAccount):
    user = models.OneToOneField(UserAccount.user)
    maritalStatus = models.BooleanField

#EmergencyInfo is a model to handle emergency info
class EmergencyInfo():
    name = models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    relation = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)