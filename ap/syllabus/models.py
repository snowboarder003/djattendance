from django.db import models
from classes.models import Class
from books.models import Book

from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager


""" SYLLABUS models.py

This module catalogs all pertinent data associated with classes in the FTTA
for use in in other functions. For example, Data includes class name, date,
assignments, books, midterms, etc. Inputted data is organized into a
readable form for the entire term.

Data Models:
    - Syllabus:
        classSyllabus (ForeignKey: Class)
    - Session:
        date
        topic
        book (ForeignKey: Book) - name(?), code
        assignment[]
        note
        exam (boolean, HIDDEN)
        syllabus (ForeignKey: Syllabus)
"""


class Syllabus (models.Model):

    # syllabus for a class; e.g. FMoC, BoC, GOW
    classSyllabus = models.ForeignKey(Class)

    # read assignment AFTER class?
    after = models.BooleanField(default=False)

    def __unicode__(self):
        return self.classSyllabus


class Session(models.Model):

    # date of the class
    date = models.DateField(verbose_name='session date')

    # topic; "exam";
    topic = models.CharField(max_length=200)

    # book name, code
    book = models.ForeignKey(Book)

    # assignment info (pages; chapters; msgs; lessons; verses; exam: "FINAL, MIDTERM, ETC")
        # can list multiple assigments, e.g. memory verses
    assignment = ArrayField(dbtype="varchar(255)")

    # exam (HIDDEN)
    exam = models.BooleanField(default=False)

    # the class syllabus this session refers to
    syllabus = models.ForeignKey(Syllabus)

    def __unicode__(self):
        """ Q: How does this work + DISPLAY? """
        return ("Class: " + self.syllabus.classSyllabus.name + "; Term: "
                + self.syllabus.classSyllabus.term + "; Date: " + self.date
                + "; Topic: " + self.topic)
