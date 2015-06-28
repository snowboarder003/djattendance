from django.db import models
from accounts.models import Trainee
from django.contrib.postgres.fields import ArrayField

""" bible_tracker models.py
The bible_tracker module is used to track a trainee's Bible reading
progress throughout the 4 terms.

DATA MODELS:
    - Weekly: class used to track the finalization of each week's bible reading.
    
    - Daily: a class used to track the status of a trainee's bible reading each day.
    Available choices are (C - Complete, M - Made up, N - No reading).

    - Tracker: a class that contains the bible books a trainee has
    completed and what year (1st or 2nd year) the book was completed for.

"""
class Weekly(models.Model):
  trainee = models.ForeignKey(Trainee, null=True)
  finalize = models.IntegerField(default=0)

class Daily(models.Model):
  week = models.ForeignKey(Weekly)
  date = models.DateField()
  status = models.CharField(max_length=1, null=True)
  def __str__(self):
    return self.status;

class Tracker(models.Model):
	trainee = models.ForeignKey(Trainee, null=True)
	firstYear = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	secondYear = ArrayField(models.CharField(max_length=100), blank=True, null=True)

