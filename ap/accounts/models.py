from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

""" accounts models.py
The user accounts module takes care of user accounts and
utilizes/extends Django's auth system to handle user authentication.

USER ACCOUNTS
    Because we want to use the user's email address as the unique
    identifier, we have chosen to implement a custom User model, 

    ...

PROFILES
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

    def create_user(self, email, password=None):
        """ Creates a user, given an email and a password (optional) """

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=APUserManager.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """ Creates a super user, given an email and password (required) """

        user = self.create_user(email, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractUser):
    """ a basic user account, with all common user information """
 
    # names
    firstname = models.CharField(max_length=30, blank=True)

    lastname = models.CharField(max_length=30, blank=True)

    middlename = models.CharField(max_length=30, blank=True)

    nickname = models.CharField(max_length=30, blank=True)

    maidenname = models.CharField(max_length=30, blank=True)

    def _get_full_name(self):
        return self.firstname + " " + self.lastname

    fullname = property(_get_full_name)

    # age, gender, etc.
    date_of_birth = models.DateField()

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


    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    gender = models.CharField(max_length=1, choices=GENDER)

    married = models.BooleanField()

    def save(self, *args, **kwargs):
        """
        Override save() method so that username always matches the user's email
        handle (minus the domain name).
        e.g. jerome@ftta.org will simply become jerome and jonathan.tien@gmail.comm
        becomes simply jonathan.tien
        """
        self.username = self.email.split('@')[0]
        super(User, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return fullname


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

    services = models.ManyToManyField(Service)

    house = models.ManyToManyField(House)

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

    # refers to the user's home address, not their training residence
    address = models.ForeignKey(Address)

    bunk = models.ForeignKey(Bunk)

    vehicle = models.ForeignKey(Vehicle)

    # flag for trainees taking their own attendance
    # this will be false for 1st years and true for 2nd with some exceptions.
    selfAttendance = models.BooleanField()


