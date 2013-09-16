from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

""" accounts models.py
The user accounts module takes care of user accounts and
utilizes/extends Django's auth system to handle user authentication.

Because we want to use the user's email address as the unique
identifier, we have chosen to implement a custom User model
(extending Django's AbstractBaseUser), which handles authentication and
also includes all basic/common user information.

User accounts are extended by Profiles, which contain additional information,
generally representing roles that various users fill. The two most common
ones, Trainee and TA, are implemented here. Other examples include:
    - every Trainee is also a service worker, so those user accounts also
    have a ServiceWorker profile that contains information needed for the
    ServiceScheduler algorithm
    - before coming to the FTTA, a trainee may have come to short-term. 
    These trainees will have a Short-Term profile at that time, and later
    also have a Trainee  profile when they come for the full-time.

The usage of profiles allows user to have multiple roles at once, and also
allows a clean transition between roles (e.g. a Short-termer who becomes a
Trainee and then later a TA can keep the same account throughout).
"""

class APUserManager(BaseUserManager):
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        # user's default password is date of birth
        # formatted: '2013-09-16' (yyyy-mm-dd)
        user.set_password(str(date_of_birth))
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """ a basic user account, with all common user information """

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = MyUserManager()

    firstname = models.CharField(max_length=30, blank=True)

    lastname = models.CharField(max_length=30, blank=True)

    middlename = models.CharField(max_length=30, blank=True)

    nickname = models.CharField(max_length=30, blank=True)

    maidenname = models.CharField(max_length=30, blank=True)

    # date of birth
    date_of_birth = models.DateField()

    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

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

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    def get_short_name(self):
        return self.firstname

    def __unicode__(self):
        return self.email


class Profile(models.Model):
    """ A profile for a user account, containing user data. A profile can be thought
    of as a 'role' that a user has, such as a TA, a trainee, or a service worker.
    Profile files should be pertinent directly to that profile role. All generic
    data should either be in this abstract class or in the User model.
    """

    # each user should only have one of each profile
    account = models.OneToOneField(User)

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


