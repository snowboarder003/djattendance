from django.db import models
from datetime import date
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
		return self.account.trainee.current_term
	
	name = property(trainee_name)
	house = property(trainee_house)
	term = property(trainee_term)


class RosterManager(models.Manager):
	# when roster is created in admin, admin calls RosterAdmin.save_related()
	# to add the unreported houses.
	def create_roster(self, date):
		roster = self.create(date=date)
		roster.save() # have to save before adding many-to-many relationship
		# initialize with all houses unreported (remove houses from list when hc submits form).
		for house in House.objects.all(): 
			roster.unreported_houses.add(house)
		roster.save()
		return roster


class Roster(models.Model):
	date = models.DateField(primary_key=True)
	
	objects = RosterManager()
	unreported_houses = models.ManyToManyField(House, related_name= 'rosters', blank=True, null=True)

	def __unicode__(self):
		return self.date.strftime("%m/%d/%Y")


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
	comments = models.CharField(max_length=250, blank=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __unicode__(self):
		return self.absentee
	
	