from django.db import models
# from datetime import date

# #import from djorm-ext-pgarray for Postgres array field for Django
# from djorm_pgarray.fields import ArrayField
# from djorm_expressions.models import ExpressionManager

#import from other apps
from accounts.models import Profile
from houses.models import House

""" absent_trainee_roster models.py
The absent trainee roster module takes care of generating daily absent trainee rosters
from HC imported forms.

Trainee information is extended from the user account model
"""

class Absentee(Profile):
	
	def __unicode__(self):
		return self.account.get_full_name()
	
	def trainee_name(self):
		return self.account.get_full_name()
	
	def trainee_house(self):
		return self.account.trainee.house
	
	def trainee_term(self):
		return self.account.trainee.term
	
	name = property(trainee_name)
	house = property(trainee_house)
	term = property(trainee_term)


class Roster(models.Model):
	date = models.DateField(primary_key=True)
	unreported_houses = models.ManyToManyField(House)


class Entry(models.Model):
	
	ABSENT_REASONS = (
        ('C', 'Conference'), 
        ('SI', 'Sick'),
        ('SE', 'Service'),
        ('O', 'Other'),
        ('T', 'Out of Town'),
        ('NA', 'Sick - Not absent'),
        ('F', 'Fatigue'),
    )
	
	roster = models.ForeignKey(Roster)
	absentee = models.ForeignKey(Absentee)
	reason = models.CharField(max_length=2, choices=ABSENT_REASONS)
	comments = models.CharField(max_length=250)
