from rest_framework import serializers
from .models import User, Trainee, TrainingAssistant


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class TraineeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainee


class TrainingAssistantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingAssistant
