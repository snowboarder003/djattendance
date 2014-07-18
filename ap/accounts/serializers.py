from rest_framework import serializers
from .models import User, Trainee, TrainingAssistant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee


class TrainingAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingAssistant
