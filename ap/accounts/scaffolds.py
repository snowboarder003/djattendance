import string
import random

import scaffolding

from accounts.models import User, TrainingAssistant, Trainee
from aputils.models import Vehicle, Address, EmergencyInfo
from terms.models import Term
from teams.models import Team
from houses.models import House, Bunk
from services.models import Service

def email_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size)) + "@email.com"

class UserScaffold(object):

    email = scaffolding.Name
    firstname
    lastname
    gender
    date_of_birth

scaffolding.register(User, UserScaffold)

class TrainingAssistantScaffold(object):