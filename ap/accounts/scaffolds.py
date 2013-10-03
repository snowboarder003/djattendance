import string, random
from datetime import date

import scaffolding
from scaffodling import Tube

from accounts.models import User, TrainingAssistant, Trainee
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

def email_generator(size=8, chars=string.ascii_lowercase + string.digits):
    yield ''.join(random.choice(chars) for x in range(size)) + "@email.com"

class UserScaffold(object):

    email = scaffolding.RandomEmail(length=8, domain="email.com")
    firstname = scaffolding.FirstName(max_length=32)
    lastname = scaffolding.LastName(max_length=32)
    gender = scaffolding.RandomValue(lst=['B', 'S'])
    date_of_birth = scaffolding.RandomDate(date(1960, 1, 1), date.today())

scaffolding.register(User, UserScaffold)

# class TrainingAssistantScaffold(object):