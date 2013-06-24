from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import UserAccount

# Create your models here.

class TrainintgAssistantAccount(AbstractUser):
    user = models.OneToOneField(UserAccount.user)
    maritalStatus = models.BooleanField
    residence = models.CharField(max_length=30)
   
