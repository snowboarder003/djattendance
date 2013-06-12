from django.db import models

""" LOCALITIES models.py

The Localities module is a utility module underlying other apps. In particular,
both trainees are related to localities (as being sent from), and teams are
related to localities (as serving in).

Data Models:
    - Locality: a local church

"""


class Locality(models.Model):

    city = models.CharField(max_length=50)

    # optional for non US localities
    state = models.CharField(max_length=2, blank=True, choices=STATES)

    # for non US localities
    province = models.CharField(max_length=30, blank=True)

    country = models.CharField(max_length=5, choices=COUNTRIES)

    STATES = (
        ('AL','Alabama'),
        ('',''),
    )

    COUNTRIES = (
        ('USA', 'United States'),
        ('NZ', 'New Zealand'),
        ('AUS', 'Australia'),
        ('CAN', 'Canada'),
        ('CHN', 'China'),
    )

