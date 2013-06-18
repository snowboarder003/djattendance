from django.db import models
import datetime

########################################################################80chars

""" TERM models.py

This schedules module is for representing weekly trainee schedules.

Data Models
- Term:
    a term of the full-time training, consisting of twenty weeks

"""


class Term(models.Model):

    # a term's long name; i.e. Fall 2013, Spring 2015
    name = models.CharField(max_length=12)

    # a term's short code; i.e. Fa13, Sp15
    code = models.CharField(max_length=4, primary=True)

    # first day of the term, the monday of pre-training
    start = models.DateField()

    # the last day of the term, the sat of semiannual
    end = models.DateField()

    # returns an absolute date for a term week/day pair
    def getDate(self, week, day):
        return self.start + datetime.timedelta(week * 7 + day)

    # returns a term week/day pair for an absolute date
    def reverseDate(self, date):
        if self.start <= date <= self.end:
            # days since the term started
            delta = date - self.start
            return (delta/7, delta%7)
        # if not within the dates the term, return invalid result
        else:
            return (-1, -1)