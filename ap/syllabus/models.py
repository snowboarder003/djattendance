from django.db import models
from classes.models import Class
from books.models import Book

from time import strftime

from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager

from django.core.urlresolvers import reverse, reverse_lazy

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
    class_syllabus = models.OneToOneField(Class)
    # whether assignment is read before or after class (== true)
    after = models.BooleanField(default=False)

    def __unicode__(self):
        return "[{term}] {name}".format(term=self.class_syllabus.term.name, 
                                         name=self.class_syllabus.name)


class Session(models.Model):
    syllabus = models.ForeignKey(Syllabus)
    date = models.DateField(verbose_name='session date')
    topic = models.CharField(max_length=255)
    exam = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return "[{date}] {topic}".format(date=self.date, topic=self.topic)


class Assignment(models.Model):
    session = models.ForeignKey(Session)
    book = models.OneToOneField(Book)
    reading = models.CharField(max_length=255)

    def __unicode__(self):
        return "{book} {reading}".format(book=self.book.name, reading=self.reading)
