from django.db import models

""" UTILS models.py

The UTILS model handles various miscellaneous data models that will be used
widely across other files.

Data Models:
	- Country: A standard country, used in cities.
	- City: A standard city anywhere in the world, used in localities and
    addresses
    - Address: A standard US address used for training residences, emergency
    contact information, and other things
    - Vehicle: Represents vehicles owned by trainees
"""


class Country(models.Model):

	# the name of the country
	name = models.CharField(max_length=50)


class City(models.Model):

	# the name of the city
	name = models.CharField(max_length=50)
	
	# state or province (depending on which country it is)
	region = models.CharField(max_length=30)

	# Country foreign key
	country = models.ForeignKey(Country)


class Address(models.Model):
	# line 1 of the address field
	address1 = models.CharField(max_length=150)
	
	# line 2 of the address field
	address2 = models.CharField(max_length=150, blank=True)
	
	# City foreign key
	city = models.ForeignKey(City)
	
	zip_code = models.SmallIntegerPositiveField()

	# optional four-digit zip code extension
	zip_4 = models.SmallPositiveIntegerField(blank=True)

	# optional details field
	details = models.CharField(max_length=150)


class Vehicle(models.Model):
	
	# e.g. Honda, Toyota
	make = models.CharField(max_length=30)
	
	# e.g. Accord, Camry
	model = models.CharField(max_length=30)
	
	license_plate = models.CharField(max_length=10)
