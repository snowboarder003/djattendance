from django.db import models
from classes.models import Class
from books.models import Book


"""" SYLLABUS models.py

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
        assignment
        note
        exam (boolean, HIDDEN)
        syllabus (ForeignKey: Syllabus)
"""


class Syllabus (models.Model):

    # syllabus for a class; e.g. FMoC, BoC, GOW
    classSyllabus = models.ForeignKey(Class)  # should this be ManyToMany relationship?

    def __unicode__(self):
        return self.classSyllabus


class Session(models.Model):

    # date of the class
    """ Q: How does datefield work? """
    date = models.DateField(verbose_name='session date')

    # topic; "exam";
    topic = models.TextField()

    # book name, code
    book = models.ForeignKey(Book)

    # assignment info (pages; chapters; msgs; lessons; verses; exam: "FINAL, MIDTERM, ETC")
        # can list multiple assigments, e.g. memory verses
    assignment = models.TextField()

    # extra assignment;
    note = models.TextField()

    # exam (HIDDEN)
    exam = models.BooleanField()

    # which syllabus does this session refer to?
    syllabus = models.ForeignKey(Syllabus)

    def __unicode__(self):
        return self.date
