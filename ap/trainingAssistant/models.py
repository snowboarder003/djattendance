from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TrainintgAssistantAccount(AbstractUser):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    birthday = models.DateField
    maritalStatus = models.BooleanField
    residence = models.CharField(max_length=30)
   
