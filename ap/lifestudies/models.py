import datetime

from django.db import models
from accounts.models import Trainee
from books.models import Book
from django.core.exceptions import ValidationError

""" DISCIPLINE models.py

This discipline module handles the assigning of reading (mainly life-studies) summaries for disciplinary purposes.

Data Models
- Discipline:
    a discipline assigned to a trainee

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
    infraction = models.CharField(max_length=30, default="attendance")

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
        return self.trainee.account.get_full_name() + " | " + self.infraction + " | " + self.offense
    
    def displayForTrainee(self):
        return "Life-Study Summary due as " + self.offense + "for " + self.infraction + " infraction"

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
    discipline = models.ForeignKey(Discipline)

    # automatically generated date when summary is submitted
    date_submitted = models.DateTimeField(blank=False, null=True)

    def __unicode__(self):
        return self.trainee.account.get_full_name()  + " | " + self.book + " | " + self.chapter

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

    """These methods were from the original file"""
    # @staticmethod
    # def current_term():
    #     """ Return the current term """
    #     try:
    #         return Term.objects.get(Q(start__lte=datetime.date.today()), Q(end__gte=datetime.date.today()))
    #     # this will happen in cases such as in-between terms (or empty DB, possibly)
    #     except ObjectDoesNotExist:
    #         # return an obviously fake term object
    #         return Term(name="Temp 0000", code="TM00", start=datetime.date.today(), end=datetime.date.today())


    # def getDate(self, week, day):
    #     """ return an absolute date for a term week/day pair """
    #     return self.start + datetime.timedelta(week * 7 + day)

    # def reverseDate(self, date):
    #     """ returns a term week/day pair for an absolute date """
    #     if self.start <= date <= self.end:
    #         # days since the term started
    #         delta = date - self.start
    #         return (delta / 7, delta % 7)
    #     # if not within the dates the term, return invalid result
    #     else:
    #         return (-1, -1)

    # def get_absolute_url(self):
    #     return reverse('terms:detail', kwargs={'code': self.code})

    # def __unicode__(self):
    #     return self.name
