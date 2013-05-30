from django.db import models

""" TEAMS app

The teams app is responsible for representing teams in data. This is a utility
class used by many other applications

Data Models:
    Team: an FTTA team
"""

class Team(Models.model):

    TEAM_TYPES = (
        ('CAMPUS', 'Campus')
        ('CHILD', 'Children')
        ('COM', 'Community')
        ('YP', 'Young People')
        ('I', 'Internet')
    )

    # the full name of a team, e.g. Irvine Young People, or Anaheim Community
    name = models.CharField(max_length=50)

    # the abbreviation of the team, e.g. I-YP or ANA-COM
    shortcode = models.CharField(max_length=10)

    type = models.CharField(max_length=6, choices=TEAM_TYPES)
