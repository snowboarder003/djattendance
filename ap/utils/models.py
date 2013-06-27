from django.db import models

""" UTILS models.py

The UTILS model handles various miscellaneous data models that will be used
widely across other files.

Data Models:
    - Address: A standard US address used for training residences, emergency
    contact information, and other things
    - City: A standard city anywhere in the world, used in localities and
    addresses
    - Vehicle: Represents vehicles owned by trainees
"""


class Address(models.Model):
	# line 1 of the address field
	address1 = models.CharField(max_length=150)
	
	# line 2 of the address field
	address2 = models.CharField(max_length=150)
	
	# City foreign key
	city = models.ForeignKey(City)
	
	zipCode = models.CharField(max_length=5)

	# optional four-digit zip code extension
	zip4 = models.CharField(max_length=4)

	# optional details field
	details = models.CharField(max_length=150)


class City(models.Model):

	# the name of the city
	name = models.CharField(max_length=50)
	
	# state or province (depending on which country it is)
	stateOrProvince = models.CharField(max_length=30)

	country = models.CharField(max_length=50)


class Vehicle(models.Model):
	
	make = models.CharField(max_length=30)
	
	model - models.CharField(max_length=30)
	
	licensePlate = models.CharField(max_length=10)

	# Trainee foreign key (will uncomment when imported)
	# trainee = models.ForeignKey(Trainee.Trainee)
