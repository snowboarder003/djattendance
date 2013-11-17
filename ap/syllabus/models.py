from django.db import models
from classes.models import Class
from books.models import Book

from time import strftime

from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager

from django.core.urlresolvers import reverse




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

    #start = models.DateField(verbose_name='start date')

    # read assignment AFTER class?
    after = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     """ (1) TO DO: Figure out how this gets the URL code for about.html 
    #                 This turns into P<code>Fa|Sp \d{2} object for the URL...?
    #     """
    #     return "/syllabus/%i/" % self.classSyllabus.code
    #     #return reverse('syllabus:detail', kwargs={'code': self.classSyllabus.code})
    def get_absolute_url(self):
        # return reverse('syllabus:detail-view', kwargs={'code': self.classSyllabus.code})
        # return reverse('syllabus:classlist-view', kwargs={'code': self.classSyllabus.code})
        return reverse('self.classSyllabus.code')

    def get_url_path(self):
        return '%s/' % self.classSyllabus.code


    def __unicode__(self):
        # added Term to syllabus (already included Name)
        return (self.classSyllabus.name + " | " + self.classSyllabus.term.name)


class Session(models.Model):

    # date of the class
    date = models.DateField(verbose_name='session date')

    # topic; "exam";
    topic = models.CharField(max_length=200)

    # book name, code
    book = models.ForeignKey(Book)

    # assignment info (pages; chapters; msgs; lessons; verses; exam: "FINAL, MIDTERM, ETC")
        # can list multiple assigments, e.g. memory verses
    """ TO DO: Django Admin does not properly display ARRAY assignment
               Can currently only create one assignment;
               Should be able to create multiple assignments.
    """
    assignment = ArrayField(dbtype="varchar(255)")

    # exam (HIDDEN)
    exam = models.BooleanField(default=False)

    # the class syllabus this session refers to
    syllabus = models.ForeignKey(Syllabus)

    def __unicode__(self):
        return (self.syllabus.classSyllabus.name + " | "
                + self.syllabus.classSyllabus.term.name + " | " + 
                self.date.strftime('%Y/%m/%d') + " | " + self.topic)
