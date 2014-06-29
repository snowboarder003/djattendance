import datetime

from django.db import models
from accounts.models import Trainee
from books.models import Book
from django.core.exceptions import ValidationError
from attendance.utils import Period
from terms.models import Term
from schedules.models import Schedule

""" lifestudies models.py
This discipline module handles the assigning and managing of
the life-study summaries from the TA side and the submitting
from the trainees' side.

DATA MODELS:
    - Discipline: a discipline assigned to a trainee with the
                  infraction and with the number of summaries
                  needed  
    - Summary:    a summary that a trainee submit with the 
                  content

"""

class Discipline(models.Model):

    TYPE_OFFENSE_CHOICES = (
        ('MO', 'Monday Offense'),
        ('RO', 'Regular Offense'),
    )

    TYPE_INFRACTION_CHOICES = (
        ('AT', 'Attendance'),
        ('CI', 'Cell Phone & Internet'),
        ('MS', 'Missed Service'),
        ('S', 'Speeding'),
        ('AN', 'Alarm Noise'),
        ('G', 'Guard'),
        ('C', 'Curfew'),
        ('M', 'Misplaced Item'),
        ('HI', 'House Inspection'),
        ('L', 'Library'),
        ('MISC', 'Misc'),
    )

    # an infraction is the reason for the trainee to be assigned discipline
    # The longest string will be "Additional Monday Discipline" (28 characters)
    infraction = models.CharField(choices=TYPE_INFRACTION_CHOICES,
        max_length=30)

    # a quantity refers to how many summaries are assigned
    quantity = models.PositiveSmallIntegerField(blank=False, null=False)

	# the date of the assignment of the discipline.
    date_assigned = datetime.datetime.now()

    # the due date and time for the discipline to be submitted by
    due = models.DateField(blank=False, null=False)

    # the type of offense being assigned
    offense = models.CharField(choices=TYPE_OFFENSE_CHOICES, default='RO', 
        blank=False, null=False, max_length=20)

    # relationship: many discplines to one specific trainee
    # even for assigning house, each trainee has one discipline
    trainee = models.ForeignKey(Trainee)

    # To add the specified number of life-studies to a trainee
    # See information manual for when to add additional discipline
    #   When you automatically assign discipline
    def addSummary(self, num):
        self.quantity += num
        if num < 0 :
            return self
        return self

    def approveAllSummary(self):
        for summary in self.summary_set.all():
            summary.approve()
        self.save()
        return self.summary_set.all()

    """TODO"""
    def changeDueDate(self, date):
        if date < datetime.today().date():
            #raise exception or return error
            return self
        else :
            self.due = date
            return self

    """get the number of summary that still needs to be submitted"""
    def getNumSummaryDue(self):
        return self.quantity - len(self.summary_set.all())

    def getNumSummaryApproved(self):
        num = 0
        for summary in self.summary_set.all():
            if summary.approved == True:
                num = num + 1
        return num

    #if this is True it means all the lifestudies has been approved and all have been submitted
    #this assume num of summary submitted not larger than num of summary assigned
    def isCompleted(self):
        if self.getNumSummaryDue() > 0:
            return False
        else: 
            for summary in self.summary_set.all():
                if summary.approved == False:
                    return False
        return True

    #use calculateSummary(8,9,6) for now
    """this function examines the Schedule belonging to trainee and search through all
    the Events and Rolls. Returns the number of summary a trainee needs to be assigned
    over the given period."""
    @staticmethod
    def calculateSummary(trainee, period):
        num_A = 0
        num_T = 0
        num_summary = 0
        for roll in trainee.rolls.all():
            if roll.event.date >= Period().start(period) and roll.event.date <= Period().end(period):
                if roll.status == 'A':
                    num_A += 1
                elif roll.status == 'L' or roll.status == 'T' or \
                     roll.status == 'U':
                    num_T += 1
        if num_A >= 2:
            num_summary += num_A
        if num_T >= 5:
            num_summary += num_T - 3
        return num_summary

    def __unicode__(self):
        return self.trainee.account.get_full_name() + ' | ' + self.infraction + ' | ' + self.offense + ' | ' + str(self.quantity) + ' | ' + str(self.getNumSummaryDue()) + ' | ' + str(self.isCompleted())

class Summary(models.Model):
	# the content of the summary (> 250 words)
    content = models.TextField()

	# the book assigned to summary
    # relationship: many summaries to one book
    book = models.ForeignKey(Book)

	# the chapter assigned to summary
    chapter = models.PositiveSmallIntegerField(blank=False, null=False)

	# if the summary has been approved
    approved = models.BooleanField(default=False)

	# which discipline this summary is associated with
    discipline = models.ForeignKey(Discipline)

    # automatically generated date when summary is submitted
    date_submitted = models.DateTimeField(editable=False, null=True, auto_now_add=True)

    def __unicode__(self):
        return self.discipline.trainee.account.get_full_name()  + ' | Book: ' + self.book.name + ' | Chapter: ' + str(self.chapter) + ' | Approved: ' + str(self.approved)

    def approve(self):
        self.approved = True
        self.save()
        return self
   

