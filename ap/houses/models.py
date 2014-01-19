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
        ('S', 'Sister'),
        ('C', 'Couple')
    )

    # the common name for the house, e.g. 1329 Amberwick, 2102 Grace
    name = models.CharField(max_length=50)

    # the house's address (defined in the utils class)
    address = models.ForeignKey(Address)

    # whether this is a brother's house or a sister's house
    gender = models.CharField(max_length=1, choices=GENDER)

    # whether this house is actively used by the training
    used = models.BooleanField()
    
    #returns a query set of the empty bunks for this house
    def empty_bunk_count(self,position_list=[]):
        if len(position_list)==0:
            return Bunk.objects.filter(room__house=self).exclude(trainee__active=True).count()
        return Bunk.objects.filter(room__house=self,position__in=position_list).exclude(trainee__active=True).count()

    def __unicode__(self):
        return u' %s' % (self.name)


class Room(models.Model):

    ROOM_TYPES = (
        ('LIV', 'Living Room'),
        ('BED', 'Bedroom'),
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


class BedFrameType(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class MattressType(models.Model):
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
    
    bed_frame_type = models.ForeignKey(BedFrameType, null=True, blank=True)
    
    mattress_type = models.ForeignKey(MattressType, null=True, blank=True)
    #End of MS access db fields
    

    # the bunk's number
    number = models.SmallIntegerField()

    # whether this is a top or bottom bunk
    position = models.CharField(max_length=1, choices=POSITION)

    link = models.OneToOneField('Bunk', null=True, blank=True)

    # which room this bunk is in
    room = models.ForeignKey(Room)
    
    #from Access db
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.room.house.name + " Bunk " + str(self.number)
    
