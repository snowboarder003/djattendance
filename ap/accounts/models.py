from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

""" accounts models.py
The user accounts module takes care of user accounts for the attendance+ and
utilizes/extends Django's auth system to handle user authentication.

There are several different kinds of users
    - Trainee: a regular (full-time) trainee at the FTTA
    - TrainingAssistant: a TA
    - ShortTermTrainee: a short-termer (that stays for longer than 2 weeks).
                        this is used to assign services to short-termers
    - HospitalityGuest: this is for those who take LSM hospitality during the
                        semiannual training. they will be assigned services

Each of these users is extended from UserAccount, which itself is extended from
django's AbstractUser.
"""


class UserAccount(AbstractUser):
    """ a basic user account, with all common user information """

    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    #optional middle name. First and last are in the abstract
    middleName = models.CharField(max_length=30, blank=True)

    nickname = models.CharField(max_length=30, blank=True)

    maidenName = models.CharField(max_length=30, blank=True)

    birthdate = models.DateField()

    gender = models.CharField(max_length=1, choices=GENDER)

    # refers to the user's home address, not their training residence
    address = models.ForeignKey(Address)

    #return the age based on birthday
    def _get_age(self):
        today = date.today()
        birth = date.fromtimestamp(self.birthdate)
        try:
            birthday = birth.replace(year=today.year)
        except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
            birthday = birth.replace(year=today.year, day=birth.day-1)
        if birthday > today:
            return today.year - birth - 1
        else:
            return today.year - birth

    age = property(_get_age)

    married = models.BooleanField()

class Profile(models.Model):
    """ A profile for a user account, containing user data. A profile can be thought
    of as a 'role' that a user has, such as a TA, a trainee, or a service worker.
    Profile files should be pertinent directly to that profile role. All generic
    data should either be in this abstract class or in the User model.
    """

    # each user account account can have multiple profiles
    account = models.ForeignKey(UserAccount)

    # whether this profile is still active
    # ex: if a trainee becomes a TA, they no longer need a service worker profile
    active = models.BooleanField()

    date_created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class TrainingAssistant(Profile):

    oversees = models.ManyToManyField(Service)

class Trainee(Profile):

    TRAINEE_TYPES = (
        ('R', 'Regular (full-time)'),  # a regular full-time trainee
        ('S', 'Short-term (long-term)'),  # a 'short-term' long-term trainee
        ('C', 'Commuter')
    )

    # many-to-many because a trainee can go through multiple terms
    term = models.ManyToManyField(Term)

    type = models.CharField(max_length=1, choices=TRAINEE_TYPES)

    spouse = models.OneToOneField('self', blank=True)

    emergencyInfo = models.OneToOneField(EmergencyInfo)

    TA = models.ForeignKey(TrainingAssistant)

    dateBegin = models.DateField()

    dateEnd = models.DateField()

    mentor = models.ForeignKey('self', related_name='mentee')

    team = models.ForeignKey(Team)

    services = models.ManyToManyField(Service)

    house = models.ForeignKey(House)

    bunk = models.ForeignKey(Bunk)

    vehicle = models.ForeignKey(Vehicle)

    # flag for trainees taking their own attendance
    # this will be false for 1st years and true for 2nd with some exceptions.
    selfAttendance = models.BooleanField()
