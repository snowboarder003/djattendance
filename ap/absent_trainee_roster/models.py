from django.db import models
from datetime import timedelta
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
        ('F', 'Fatigue'),
    )
	
	roster = models.ForeignKey(Roster)
	absentee = models.ForeignKey(Absentee)
	reason = models.CharField(max_length=2, choices=ABSENT_REASONS)
	coming_to_class = models.BooleanField(default=False)
	comments = models.CharField(max_length=250, blank=True)

	# second integer is a flag for the '+' in days absent report.
	# -if the flag is 0, then the house was reported all previous 7 days.
	# -if the flag is 1, then the house was unreported within the past 7 days,
	#  and the entry should have a '+' in days absent.
	# days_absent = models.IntegerField()
	# flag_unreported = models.BooleanField(default=False)

	# def calc_days_absent(self):
	# 	days = 1
	# 	unreported = False
	# 	date = self.roster.date
	# 	for i in range(1,7):
	# 		date = date - timedelta(days=1)
	# 		try:
	# 			prev_roster = Roster.objects.get(date=date)
	# 		except:
	# 			pass
	# 		else:
	# 			if self.absentee.house in prev_roster.unreported_houses.all():
	# 				unreported = True
	# 			else:
	# 				for entry in prev_roster.entry_set.all():
	# 					if self.absentee == entry.trainee:
	# 						days += 1
	# 	return (days, unreported)

	# def save(self):
	# 	# super(Entry, self).save()
	# 	# asdf = self.calc_days_absent()
	# 	# print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
	# 	# print(asdf)
	# 	# (self.days_absent, self.flag_unreported) = self.calc_days_absent()
	# 	super(Entry, self).save()

	class Meta:
		verbose_name_plural = 'entries'

	def __unicode__(self):
		return self.absentee.name
	
	
