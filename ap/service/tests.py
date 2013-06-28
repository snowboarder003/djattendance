from django.test import TestCase
from service.models import category, service, period, instance


class ServiceTest(TestCase):
    def setup(self):
    	category.objects.create()

    def test_service_can_speak(self):
    	""" service objects that can speak are correctly identified """
    		
