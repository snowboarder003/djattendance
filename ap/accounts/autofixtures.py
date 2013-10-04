from accounts.models import User, TrainingAssistant, Trainee
from autofixture import generators, register, AutoFixture


class UserAutoFixture(AutoFixture):
    field_values = {
    }

register(User, UserAutoFixture)


class TraineeAutoFixture(AutoFixture):
	field_values = {
    }

register(Trainee, TraineeAutoFixture)


class TrainingAssistantAutoFixture(AutoFixture):
	field_values = {
    }

register(TrainingAssistant, TrainingAssistantAutoFixture)
