"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

"""
class SimpleTest(TestCase):
    def test_basic_addition(self):
        
        Tests that 1 + 1 always equals 2.
    
        self.assertEqual(1 + 1, 2)
"""
from houses.models import House

class HouseAddressTests(TestCase):
	def setUp(self):
		House.objects.create(name="Sarah", address1="2119 Grace", address2="Cambridge", gender="f", used=True)

	def test_address_returns_right_value(self):
		"""
		House.address should return the concatenated value 
		of address1 and address1
		"""
		h=House.objects.get(name="Sarah")
		house_address = h.address
		con_address =h.address1 + "\n" + h.address2
		self.assertEqual(house_address, con_address)