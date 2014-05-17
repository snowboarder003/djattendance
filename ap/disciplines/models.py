import datetime

from django.db import models
from accounts.models import Trainee
from books.models import Book


""" DISCIPLINE models.py

This discipline module handles the assigning of reading (mainly life-studies) summaries for disciplinary purposes.

Data Models
- Discipline:
    a discipline assigned to a trainee

"""


class Discipline(models.Model):
    MO = 'Monday Offense'
    RO = 'Regular Offense'

    # an infraction is the reason for the trainee to be assigned discipline
    # The longest string will be "Additional Monday Discipline" (28 characters)
    infraction = models.CharField(max_length=30, default="attendance")

    # a quantity refers to how many summaries are assigned
    quantity = models.PositiveSmallIntegerField(blank=False, null=False)

	# the date of the assignment of the discipline.
    date_assigned = models.datetime.datetime.now()

    # the due date and time for the discipline to be submitted by
    due = models.DateTimeField(blank=False, null=False)

    # the type of offense being assigned
    """TODO use choices here"""
    offense = models.CharField(default=RO, blank=False, null=False, max_length=20)

    # the last day of the term, the sat of semiannual
    trainee = models.ForeignKey(Trainee)

    def __unicode__(self):
        return self.offense + " | " + self.infraction + " | " + self.trainee.name

    """TODO: fix the syntax of this code, this code doesn't compile"""
    def addSummary(self, num):
        self.quantity += num
        if num < 0 :
            #raise exception or return error?
            return self
        else :
            for i in range(num) :
                self.summary_set.create()
        return self

    """TODO: to check if the date is in the past"""
    def changeDueDate(self, date):
        self.due = date
        return self

    """TODO: This also needs to be tested to see if it works"""
    def getIncompleteSummary(self):
        return self.summary_set.all().filter(date_submitted != Null).count()

    # comments: method to calculate period. Do they need to be editable by TA?

class Summary(models.Model):
	# the content of the summary (> 250 words)
	content = models.TextField()

	# the book assigned to summary
	book = models.ForeignKey(Book)

	# the chapter assigned to summary
	chapter = models.PositiveSmallIntegerField(blank=False, null=False)

	# if the summary has been approved
	approved = models.BooleanField(default=False)

	# which discipline this summary is associated with
	discipline = models.ForeignKey(Discipline)

    def __unicode__(self):
        return self.book + " | " + self.chapter + " | " + self.discipline.trainee.name

    """TODO: to do these methods"""
    # def updateContent(self, string):
    #     self.content = string
    #     return self

    # def approve(self):
    #     self.approved = True
    #     return self

    # def submit(self):


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
