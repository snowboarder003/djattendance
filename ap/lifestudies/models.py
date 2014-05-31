import datetime

from django.db import models
from accounts.models import Trainee
from books.models import Book
from django.core.exceptions import ValidationError

""" LifeStudy models.py

This LifeStudy module handles the assigning of reading (mainly life-studies) summaries for disciplinary purposes.

Data Models
- LifeStudy:
    a LifeStudy assigned to a trainee

"""


class LifeStudy(models.Model):
    
    MONDAYOFFENSE = 'MO'
    REGULAROFFENSE = 'RO'

    TYPE_OFFENSE_CHOICES = (
        (MONDAYOFFENSE, 'Monday Offense'),
        (REGULAROFFENSE, 'Regular Offense'),
    )

    # an infraction is the reason for the trainee to be assigned discipline
    # The longest string will be "Additional Monday Discipline" (28 characters)
    infraction = models.CharField(max_length=30, default='attendance')

    # a quantity refers to how many summaries are assigned
    quantity = models.PositiveSmallIntegerField(blank=False, null=False)

	# the date of the assignment of the discipline.
    date_assigned = datetime.datetime.now()

    # the due date and time for the discipline to be submitted by
    due = models.DateField(blank=False, null=False)

    # the type of offense being assigned
    offense = models.CharField(choices=TYPE_OFFENSE_CHOICES, default=REGULAROFFENSE, 
        blank=False, null=False, max_length=20)

    # relationship: many discplines to one specific trainee
    # even for assigning house, each trainee has one discipline
    trainee = models.ForeignKey(Trainee)

    def __unicode__(self):
        return self.trainee.account.get_full_name() + ' | ' + self.infraction + ' | ' + self.offense + ' | ' + str(self.quantity)

    def displayForTrainee(self):
        return 'Life-Study Summary due as ' + self.offense + ' for ' + self.infraction + ' infraction'

    # To add the specified number of life-studies to a trainee
    # See information manual for when to add additional discipline
    #   When you automatically assign discipline
    def addSummary(self, num):
        self.quantity += num
        if num < 0 :
            #raise exception or return error
            return self
        return self

    # for TAs to change discipline count (post-assignment case)
    def editSummary(self, num):
        if num < 0 :
            #raise exception or return error
            return self
        self.quantity = num
        return self    
    
    def changeDueDate(self, date):
        if date < datetime.today().date():
            #raise exception or return error
            return self
        else :
            self.due = date
            return self

    """TODO: This also needs to be tested to see if it works"""
    def getNumIncompleteSummary(self):
        return quantity - self.summary_set.all().count()

    # comments: method to calculate period. Do they need to be editable by TA?

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
    lifeStudy = models.ForeignKey(LifeStudy)

    # automatically generated date when summary is submitted
    date_submitted = datetime.datetime.now()
    # date_submitted = models.DateTimeField(blank=False, null=True)

    def __unicode__(self):
        return self.lifeStudy.trainee.account.get_full_name()  + ' | ' + self.book.name + ' | ' + str(self.chapter)

    """TODO: to do these methods"""
    def updateContent(string):
        self.content = string
        return self

    def approve(self):
        self.approved = True
        return self

    def submit(self, string):
        # check the word count (<250 or not)
        self.updateContent(string)
        self.date_submitted = datetime.datetime.now()
        return self
