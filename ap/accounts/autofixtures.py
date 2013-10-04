import random

from accounts.models import User, TrainingAssistant, Trainee
from autofixture import generators, register, AutoFixture, Generator


class LastNameGenerator(Generator):
	""" Generates a last name """

	def __init__(self):
		self.surname = []

	def generate(self):
		return self.surname[random.randint(0, len(self.surname))]


class UserAutoFixture(AutoFixture):
    field_values = {
    	'email' : generators.EmailGenerator(),
    	'firstname' : ,
    	'lastname' :
    }

register(User, UserAutoFixture)


class TraineeAutoFixture(AutoFixture, generate_fk=['account']):
	field_values = {
    }

register(Trainee, TraineeAutoFixture)


class TrainingAssistantAutoFixture(AutoFixture, generate_fk=['account']):
	field_values = {
    }

register(TrainingAssistant, TrainingAssistantAutoFixture)
