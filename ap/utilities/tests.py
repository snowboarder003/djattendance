from django.test import TestCase

from utilities.models import Address, City, Country, Vehicle


def setup_country():
	"""
	Creates a mythical country, saves it, and returns it.
	"""
	country = Country(name='Lala Land', code='LLL')
	country.save()
	return country

def setup_city():
	"""
	Creates a mythical city (using a mythical country), saves it, and returns
	it.
	"""
	country = setup_country()
	city = City(
		name='Lala City',
		region='Lalalandia',
		country=country,
	)
	city.save()
	return city

def setup_address():
	"""
	Creates a mythical address (using a mythical city), saves it, and returns
	it.
	"""
	city = setup_city()
	address = Address(
		address1='1234 Main St.',
		address2='P.O. Box 1234',
		city=city,
		zip_code=12345,
		zip4=1234,
		details='Insert details here.',
	)
	address.save()
	return address

def setup_vehicle():
	"""
	Creates a hypothetical vehicle, saves it, and returns it.
	"""
	vehicle = Vehicle(
		color='dark blue',
		make='Toyota',
		model='Corolla',
		license_plate='1ABC234',
	)
	vehicle.save()
	return vehicle


class AddressTests(TestCase):

	def test_create_address(self):
		"""
		Creates a mythical address, city, and country.  This is a sanity check.
		"""
		setup_address()

	def test_delete_address(self):
		"""
		Creates a mythical address, city, and country.  Deletes the address and
		hopes that nothing goes wrong.
		"""
		address = setup_address()
		address.delete()

	def test_address_unicode_with_address1_and_address2(self):
		"""
		Ensures that the address unicode method returns the right value when
		both address1 and address2 has values.
		"""
		address = setup_address()
		correctValue = '1234 Main St.\nP.O. Box 1234'
		self.assertEqual(correctValue, address.__unicode__())

	def test_address_unicode_with_address1_only(self):
		"""
		Ensures that the address unicode method returns the right value when
		only address1 has a value.
		"""
		address = setup_address()
		address.address2 = ''
		correct_value = '1234 Main St.'
		self.assertEqual(correct_value, address.__unicode__())


class CityTests(TestCase):

	def test_create_city(self):
		"""
		Creates a mythical city and country.  This is a sanity check.
		"""
		setup_city()

	def test_delete_city(self):
		"""
		Creates a mythical city and country.  Deletes the city and hopes that
		nothing goes wrong.
		"""
		city = setup_city()
		city.delete()

	def test_city_unicode(self):
		"""
		Ensures that the City unicode method returns the right value.
		"""
		city = setup_city()
		correct_value = 'Lala City'
		self.assertEqual(correct_value, city.__unicode__())


class CountryTests(TestCase):

	def test_create_country(self):
		"""
		Creates a mythical country.  This is a sanity check.
		"""
		setup_country()

	def test_delete_country(self):
		"""
		Creates a mythical country.  Deletes the country and hopes that nothing
		goes wrong.
		"""
		country = setup_country()
		country.delete()

	def test_country_unicode(self):
		"""
		Ensures that the Country unicode method returns the right value.
		"""
		country = setup_country()
		correct_value = 'Lala Land'
		self.assertEqual(correct_value, country.__unicode__())


class VehicleTests(TestCase):

	def test_create_vehicle(self):
		"""
		Creates a hypothetical vehicle.  This is a sanity check.
		"""
		setup_vehicle()

	def test_delete_vehicle(self):
		"""
		Creates a hypothetical country.  Deletes the vehicle and hopes that 
		nothing goes wrong.
		"""
		vehicle = setup_vehicle()
		vehicle.delete()

	def test_vehicle_unicode(self):
		"""
		Ensures that the Vehicle unicode method returns the right value.
		"""
		vehicle = setup_vehicle()
		correct_value = 'dark blue Toyota Corolla'
		self.assertEqual(correct_value, vehicle.__unicode__())