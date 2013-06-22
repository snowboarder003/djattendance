from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import UserAccount
from test.test_imageop import MAX_LEN

# Create your models here.

class TraineeAccount(AbstractUser):
    user = models.OneToOneField(UserAccount.user)
    term = models.OneToOneField(term.pk)
    type = models.CharField(max_length = 30)
    spouse = models.OneToOneField(TraineeAccount.pk)
    emergencyInfo = models.OneToOneField(emergencyInfo.pk)
    dateBegin = models.DateField()
    dateEnd = models.DateField()
    degree = models.CharField(max_length=30)
    mentor = models.OneToOneField(TraineeAccount.pk)
    vehicle = models.OneToOneField(vehicle.pk)
    schedule = models.OneToOneField(schedule.pk)
    team = models.OneToOneField(team.pk)
    services = models.ManyToManyField(services.pk)
    gospelPreferences = models.CharField()
    house = models.OneToOneField(house.pk)
    TA = models.OneToOneField(TA.pk)
   
