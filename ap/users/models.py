from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccount(AbstractUser):
    user = models.OneToOneField(User)
    birthdate = models.DateField() 
    gender = models.CharField(max_length = 10) 
    address = models.CharField(max_length = 100)
    service = models.CharField(max_length = 30)
    active = models.BooleanField()
    phone_number = models.IntegerField()
    locality = models.CharField(max_length = 30)
    marital_status = models.CharField(max_length = 10)
    
