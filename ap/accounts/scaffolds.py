import string, random
from datetime import date

import scaffolding
from scaffolding import Tube

from accounts.models import User, TrainingAssistant, Trainee
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service


class RandomEmail(Tube):
    """ Return a random email """

    def __init__(self, length, domain):
        self.length = length
        self.domain = domain

    def next(self):
        return ''.join(random.choice(string.ascii_lowercase) for x in range(self.length)) + self.domain


class UserScaffold(object):

    email = RandomEmail(length=8, domain="email.com")
    firstname = scaffolding.FirstName(max_length=32)
    lastname = scaffolding.LastName(max_length=32)
    gender = scaffolding.RandomValue(lst=['B', 'S'])
    date_of_birth = scaffolding.RandomDate(date(1960, 1, 1), date.today())

scaffolding.register(User, UserScaffold)

# class TrainingAssistantScaffold(object):