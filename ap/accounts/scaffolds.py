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

class TrainingAssistantScaffold(object):

	account = scaffolding.ForeignKey(queryset=User.objects.all())
	# services = scaffolding.ForeignKeyOrNone(queryset=Service.objects.all())
	# houses = scaffolding.ForeignKeyOrNone(queryset=House.objects.all())

scaffolding.register(TrainingAssistant, TrainingAssistantScaffold)


class TraineeScaffold(object):

	account = scaffolding.ForeignKey(queryset=User.objects.all())
	type = scaffolding.RandomValue(lst=['R', 'S', 'C'])
	#  term = scaffolding.RandomValue(Term.objects.all())
	TA = scaffolding.ForeignKey(queryset=TrainingAssistant.objects.all())
	date_begin = scaffolding.RandomDate(date(1960, 1, 1), date.today())
	date_end = scaffolding.RandomDate(date(1960, 1, 1), date.today())
	mentor = scaffolding.ForeignKeyOrNone(queryset=Trainee.objects.all())
	team = scaffolding.ForeignKeyOrNone(queryset=Team.objects.all())
	house = scaffolding.ForeignKeyOrNone(queryset=House.objects.all())
	address = scaffolding.ForeignKey(queryset=Address.objects.all())
	bunk = scaffolding.ForeignKeyOrNone(queryset=Bunk.objects.all())
	vehicle = scaffolding.ForeignKeyOrNone(queryset=Vehicle.objects.all())

scaffolding.register(Trainee, TraineeScaffold)
