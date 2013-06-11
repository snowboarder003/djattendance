from django.db import models
from term.models import Term

"""" CLASSES models.py

This is a utility module that will be used by other apps, such as class notes or
class syllabi. It reprents FTTA classes such as God's Economy or Greek II.

Each instance of a Class object represents a class *for a given term*

Data Models:
    - Class: a class in the FTTA

"""


class Class(models.Model):

    CLASS_TYPE = (
        ('MAIN', 'Main'),
        ('1YR', '1st Year'),
        ('2YR', '2nd Year'),
        ('AFTN', 'Afternoon'),
    )

    # the name of this class, e.g. Full Ministry of Christ, or Character
    name = models.CharField(max_length=50)

    # the shortcode, e.g. FMoC or Char
    code = models.CharField(max_length=5)

    # which term this class is in
    term = models.ForeignKey(Term)

    # which type of class this is, e.g. Main, 1st year
    type = models.CharField(max_length=4, choices=CLASS_TYPE)
