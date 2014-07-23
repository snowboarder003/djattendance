from django.db import models

from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager

from terms.models import Term
from accounts.models import Trainee

""" seating/models.py

Template:

Chart:

Partial:
"""


class Template(models.Model):
    """ Defines an array of empty seats on top of a grid """

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    height = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()

    # coordinates where a seat should be
    seats = ArrayField(dbtype="int", dimension=2)
    objects = ExpressionManager()

    def __unicode__(self):
        return self.name

class Chart(models.Model):
    """ Defines a seating chart, built on top of a template """

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    term = models.ForeignKey(Term)

    template = models.ForeignKey(Template)

    trainees = models.ManyToManyField(Trainee, through='Seat')

    def __unicode__(self):
        return self.term + ' ' + self.name

class Seat(models.Model):
    """ Intermediate model to relate a Trainee to a seating Chart """
    trainee = models.ForeignKey(Trainee)
    chart = models.ForeignKey(Chart)

    # coordinates
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()

    def __unicode__(self):
        return "%s on %s @ (%s, %s)" % {self.trainee, self.chart, self.x, self.y }

class Partial(models.Model):
    """ Defines a subset of a seating chart. Mainly used for entering roll """

    chart = models.ForeignKey(Chart)

    # upper and lower bounds on x and y axis
    x_lower = models.SmallIntegerField()
    x_upper = models.SmallIntegerField()
    y_lower = models.SmallIntegerField()
    y_upper = models.SmallIntegerField()

    def __unicode__(self):
        return "%s from (%s, %s) to (%s, %s)" % {self.chart, self.x_lower, self.y_lower, self.x_upper, self.y_upper}
