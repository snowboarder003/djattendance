from django.db import models
from aputils.models import Address

""" HOUSES models.py

This houses module is a utility model that define training housing.

Data Models:
- House: a training house
- Bunk: a bunk (either lower of upper) in a given house
"""


class House(models.Model):

    GENDER = (
        ('B', 'Brother'),
        ('S', 'Sister')
    )

    # the common name for the house, e.g. 1329 Amberwick, 2102 Grace
    name = models.CharField(max_length=50)

    # the house's address (defined in the utils class)
    address = models.ForeignKey(Address)

    # whether this is a brother's house or a sister's house
    gender = models.CharField(max_length=1, choices=GENDER)

    # whether this house is actively used by the training
    used = models.BooleanField()

    def __unicode__(self):
        return u' %s' % (self.name)


class Room(models.Model):

    ROOM_TYPES = (
        ('LIV', 'Living Room'),
        ('BED', 'Bedroom'),
        ('BED1', 'Single Bedroom'),
        ('BED2', 'Double Bedroom'),
        ('BED3', 'Triple Bedroom'),
        ('BEDc', 'Couple\'s Bedroom'),
        ('KIT', 'Kitchen'),
        ('BATH', 'Bathroom'),
        ('GAR', 'Garage'),
        ('PAT', 'Patio'),
    )

    type = models.CharField(max_length=4, choices=ROOM_TYPES)

    capacity = models.SmallIntegerField(default=0)  # null if room is not a bedroom

    house = models.ForeignKey(House)

    floor = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return "("+str(self.id)+") "+self.house.name + " " + self.type


class BedFrame(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Mattress(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class Bunk(models.Model):

    POSITION = (
        ('B', 'Bottom'),
        ('T', 'Top'),
        ('Q', 'Queen-A'),
        ('q', 'Queen-B'),
        ('S', 'Single')
    )

    LENGTH = (
        ('R', 'Regular'),
        ('L', 'Long')
    )
    
    #MS Access db fields
    for_trainees = models.BooleanField(default=True)
    
    has_protector = models.BooleanField()
    
    has_ladder = models.BooleanField()
    
    length = models.CharField(max_length=1, choices=LENGTH)
    
    bed_frame = models.ForeignKey(BedFrame)
    
    mattress = models.ForeignKey(Mattress)
    #End of MS access db fields
    

    # the bunk's number
    number = models.SmallIntegerField(primary_key=True)

    # whether this is a top or bottom bunk
    position = models.CharField(max_length=1, choices=POSITION)

    link = models.OneToOneField('Bunk', null=True, blank=True)

    # which room this bunk is in
    room = models.ForeignKey(Room)
    
    #from Access db
    notes = models.TextField()

    def __unicode__(self):
        return self.room.house.name + " Bunk " + str(self.number)
