from rest_framework.serializers import ModelSerializer
from .models import User, Trainee, TrainingAssistant


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class TraineeSerializer(ModelSerializer):
    class Meta:
        model = Trainee


class TrainingAssistantSerializer(ModelSerializer):
    class Meta:
        model = TrainingAssistant
