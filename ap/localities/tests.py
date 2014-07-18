"""
from django.test import TestCase

from localities.models import Locality

class LocalityTest(TestCase):

    def setUp(self):
        Locality.objects.create(
            city='irvine', 
            state='CA', 
            province='', 
            country='USA'
        )

    def test_team_can_speak(self):
        l = Locality.objects.get(city='irvine') 
        self.assertEqual('irvine', l.city)
        self.assertEqual('CA', l.state)
        self.assertEqual('USA', l.country)
"""