from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Roll

class RollSerializer(ModelSerializer):
    class Meta:
        model = Roll
